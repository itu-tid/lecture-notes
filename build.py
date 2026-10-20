#!/usr/bin/env python3
"""Generate the week table in README.md from the syllabus in the Obsidian vault.

The source is `$TID_VAULT/2026-syllabus.md`, and it lives outside this repo on
purpose: it carries the `%%staff asides%%` and the `New:` / `Status:` rows,
which are notes between the people teaching the course. staff_only() strips
them before anything reaches the README.

    export TID_VAULT="…/Megavault/teaching/technical interaction design/"
    python3 build.py

The parser is also what tools/build-pdfs.py reads the week → notes mapping
through, so there is one reading of the syllabus rather than two.
"""

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
README = ROOT / "README.md"

VAULT = os.environ.get("TID_VAULT")
if not VAULT:
    sys.exit("build.py: set TID_VAULT to the course folder in the Obsidian vault — "
             "the syllabus source lives there, not in this repo")
SRC = Path(VAULT) / "2026-syllabus.md"

# Fields that exist for whoever is running the course, not for whoever is
# taking it.
STAFF_FIELDS = ("New", "Status")


# ------------------------------------------------------------------- markdown

def sections(lines, level):
    """Split lines into (heading, body-lines) at the given heading level."""
    mark = "#" * level + " "
    found, head, body = [], None, []
    for line in lines:
        if line.startswith(mark):
            if head is not None:
                found.append((head, body))
            head, body = line[len(mark):].strip(), []
        elif head is not None:
            body.append(line)
    if head is not None:
        found.append((head, body))
    return found


def fields(lines):
    """`- **Key:** value` bullets → list of (key, value), order preserved."""
    return [(m.group(1), m.group(2).strip())
            for m in (re.match(r"-\s+\*\*(.+?):\*\*\s*(.*)", ln.strip()) for ln in lines)
            if m]


def parse(text):
    top = dict(sections(text.split("\n"), 2))
    if "Weeks" not in top:
        sys.exit("build.py: the syllabus is missing its ## Weeks section")
    return {"weeks": sections(top["Weeks"], 3)}


# --------------------------------------------------------------- placeholders

def numbers(seq):
    """[3, 7, 9] → "3, 7 and 9"."""
    n = [str(x) for x in seq]
    if not n:
        return "none"
    return n[0] if len(n) == 1 else ", ".join(n[:-1]) + " and " + n[-1]


def week_facts(text):
    """Facts the prose keeps getting wrong, computed from the week cards.

    Hand-written notes drift every time the term is restructured — the design
    weeks move, a check-in appears, a lecture changes hands. Anything here can
    be written as {{name}} in the markdown and will always be right.
    """
    doc = parse(text)
    weeks, design, checkin, feedback, people = [], [], [], [], {}
    for head, body in doc["weeks"]:
        m = re.match(r"Week 0*(\d+) · [^·]+· (.+)", head)
        if not m:
            continue
        num, who = int(m.group(1)), re.sub(r"\s*\*\(.*?\)\*", "", m.group(2)).strip()
        f = dict(fields(body))
        prose = [ln.strip() for ln in body if ln.strip() and not ln.strip().startswith("- ")]
        weeks.append(num)
        if len(prose) > 1 and "Design" in prose[1]:
            design.append(num)
        if "Check-in" in f:
            checkin.append(num)
        if "Feedback" in f:
            feedback.append(num)
        people.setdefault(who, []).append(num)

    facts = {
        "design-weeks": numbers(design),
        "checkin-weeks": numbers(checkin),
        "feedback-weeks": numbers(feedback),
        "week-count": str(len(weeks)),
    }
    for who, ws in people.items():
        facts[f"weeks:{who}"] = numbers(ws)
        facts[f"count:{who}"] = str(len(ws))
    return facts


def expand(text):
    for key, value in week_facts(text).items():
        text = text.replace("{{" + key + "}}", value)
    left = set(re.findall(r"\{\{([a-z][a-z:\- ]*)\}\}", text))
    if left:
        sys.exit(f"build.py: unknown placeholder(s): {', '.join(sorted(left))}")
    return text


def staff_only(text, keep):
    """Resolve the `%%...%%` staff-aside markers.

    One markdown source, two audiences. Anything wrapped in `%%` is written for
    the teaching team — delivery notes, the reasoning behind a sequencing
    choice, who is covering what — and is dropped from the student build. Use
    it for spans *inside* a paragraph or list item, not for whole paragraphs:
    an emptied paragraph would still render as one.

    `- **New:**` and `- **Status:**` rows go the same way, by field name.
    """
    if keep:
        return re.sub(r"%%(.*?)%%", r"\1", text, flags=re.S)
    text = re.sub(r"[ \t]*%%.*?%%", "", text, flags=re.S)
    text = "\n".join(ln for ln in text.split("\n")
                     if not re.match(rf"\s*- \*\*({'|'.join(STAFF_FIELDS)}):\*\*", ln))
    return re.sub(r"\n{3,}", "\n\n", text)


# --------------------------------------------------------------------- readme

WEEKS_START = "<!-- weeks:start -->"
WEEKS_END = "<!-- weeks:end -->"


def readme_table(doc):
    """The week table on the repo's front page, generated.

    It used to be kept by hand and it drifted: in one evening it needed syncing
    three times, and it only ever carried half of what the syllabus says -- the
    notes, but not the exercise, which is the thing students asked for when they
    could not make a session. Both come from the same place now.
    """
    rows = []
    for heading, body in doc["weeks"]:
        m = re.match(r"Week 0*(\d+)\s+·\s+([^·]+)", heading)
        if not m:
            continue
        f = dict(fields(body))
        gh = f.get("GH", "").strip()
        solo = f.get("Solo", "").strip()
        solo = re.split(r"(?<=[.;])\s", solo)[0] if solo else "—"
        rows.append(f"| **{m.group(1)}** · {m.group(2).strip()} | {gh or '—'} | {solo} |")
    return ("\n".join(["| week | notes | the solo hour |", "|---|---|---|"] + rows))


def write_readme(doc):
    if not README.exists():
        return
    text = README.read_text(encoding="utf-8")
    if WEEKS_START not in text or WEEKS_END not in text:
        return
    a = text.index(WEEKS_START) + len(WEEKS_START)
    b = text.index(WEEKS_END)
    updated = text[:a] + "\n\n" + readme_table(doc) + "\n\n" + text[b:]
    if updated != text:
        README.write_text(updated, encoding="utf-8")
        print(f"{README}: week table regenerated")


if __name__ == "__main__":
    source = staff_only(expand(SRC.read_text(encoding="utf-8")), keep=False)
    write_readme(parse(source))
