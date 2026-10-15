# Team Collaboration with Git Flow

## Until now each of you had your own app; from this week the group shares one

Up to now, every one of you wrote your own to-do app, alone, in your own repo. Nobody else pushed to it, so nobody else could break it, and nobody else had to understand it.

That ends this week. Your group's project starts from one app:

1. **Choose one**: one of yours, or [`todo-26`](https://github.com/itu-tid/todo-26) as it is at `week-08-components`.
2. **Make it the group's**: put it in a GitHub organisation of your own (below).
3. **Clean it up**: pull out the service layer, find the components, as in this week's notes.
4. **Then adapt it** to the app your group is actually building.

From step 3 onwards, four or five people are changing the same code. Git already lets you do that. What it does not give you is an agreement about *how*, and that is what this note is about.

## The repo lives in an organisation the group owns, not in one student's account

Create a GitHub organisation for the group (it is free), and put the repo there. Invite everybody in the group as an owner, and invite the TID staff as well.

The alternative, which every cohort used to pick, is one student's personal repo with the others added as collaborators. It works, technically. But it is *Ada's* repo, with Ada's name in every URL, and the others feel like guests in it. In an organisation the project belongs to the group, and so does the responsibility for it.

## Git Flow gives every branch one job

Git Flow is a popular way of choreographing collaboration with Git, built around several kinds of branches, each with one job:

![The Git Flow Model](../images/The%20Git%20Flow%20Model.png)

The picture uses the original names, `develop` and `master`. In TID we use a simplified version, with today's names, and three kinds of branch:

- **`main`**: releases, the versions you hand in
- **`development`**: the group's latest work, integrated
- **feature branches**: one per piece of work in progress, one person or a pair each

The rest of this note is what each of them is for.

## A feature branch is where you are allowed to break things

When you start something (a new screen, a bug fix, pulling `shareList` into a service), branch off `development`:

```bash
git checkout development
git pull
git checkout -b share-list-service
```

Commit as often as you like. Half-finished, broken, experimental: nobody else is standing on this branch, so nobody else falls over when it breaks. That is the whole point of a branch. You break your own branch, not the one four other people are standing on.

## Nothing reaches `development` without somebody else reading it first

A finished feature goes to `development` through a **pull request**, and you tag a teammate to review it. Only after they have read it, and are happy with it, is it merged.

This is the part that matters, far more than any branch name. A review is a **quality gate**: a point that code cannot pass without a second person checking it. Two things come out of every one:

- **You get feedback**, from somebody who did not write it and so does not know what you *meant*, only what you wrote.
- **Two people know the code** instead of one. When you are ill in the week before the hand-in, somebody else can fix it.

Small pull requests get real reviews. A pull request that moves one function into a service can be read in two minutes. One that touches every file gets a ✅ from someone who scrolled past it.

## `main` contains only releases, and only the staff can change it

When `development` is in a state you would hand in, it goes to `main`, again through a pull request. But this one you do not merge yourselves: **only the TID staff can accept pull requests into `main`.** That is our quality gate, the same idea one level up.

How to set that up is left to you. GitHub calls it *branch protection*, and the settings move around every year, so look it up. What we care about is that you understand why it is there, not which checkbox does it.

## Neither `main` nor `development` is ever broken

Every cohort has had at least one team whose `main` did not compile, usually for days, usually because a branch was merged in a hurry near a deadline.

It matters more than it looks. `development` is what every teammate branches from; `main` is what the examiner clones and what your deployed app is built from. A broken shared branch is not one person's problem for an afternoon. It is everybody's problem until somebody notices.

So: pull, build, and run *before* you merge, not after. A feature branch can be broken. The branches other people stand on cannot.

## `node_modules` stays out of the repo, through `.gitignore`

`.gitignore`, in the root of the repo, lists the files Git should not track. The one that matters most is `node_modules`: hundreds of megabytes that anybody can recreate with `npm install`, and that differ from one laptop to the next. Vite's starter already ignores it. Check that yours still does before the first push to the group's repo.

Your `.env.local`, with your Back4App keys, belongs in there too. `todo-26` ignores both; if your group starts from somebody else's app, check.

## Exam Questions

### 1. Describe the three kinds of branches used in the course's Git Flow model, and what each one is for.

### 2. What is a quality gate, and where are the two quality gates in the course's Git Flow model?

### 3. Why should `node_modules` be in `.gitignore`?
