# Code Organization

## A flat `src/` works until you have to look for things

Here is `todo-26` at `week-08-components`:

```
src/
├── services/
│   ├── parse.js
│   ├── authService.js
│   ├── listService.js
│   └── todoService.js
├── AddForm.jsx
├── App.jsx
├── AuthPage.jsx
├── Home.jsx
├── ListPage.jsx
├── main.jsx
├── MyListRow.jsx
├── SharedListRow.jsx
├── TextInput.jsx
├── ToDoItem.jsx
└── ToDoList.jsx
```

Ten components and `main.jsx` in one folder, sorted alphabetically, which is to say in no order that means anything. `Home` and `TextInput` sit side by side, though one is a whole page and the other is a box around an `<input>`. Nothing in the listing says which is which. You find out by opening them.

For a project one person wrote in a few weeks, that is fine. For a group that will add a dozen screens in the next six weeks, it is not. The services already have a folder of their own, since [Pulling Out the Service Layer](Pulling-Out-the-Service-Layer.md). The components are next.

## One folder per kind of file: pages, components, services

Sort the files by what they *are*:

- **`pages/`**: one file per screen, the thing a route draws
- **`components/`**: the pieces the pages are built from
- **`services/`**: the code that talks to the backend
- **`utilities/`**: a catch-all, for what you do not know where to put yet

For `todo-26` that is:

```
src/
├── pages/
│   ├── AuthPage.jsx
│   ├── Home.jsx
│   └── ListPage.jsx
├── components/
│   ├── AddForm.jsx
│   ├── TextInput.jsx
│   ├── MyListRow.jsx
│   ├── SharedListRow.jsx
│   └── ToDoList/
│       ├── ToDoList.jsx
│       └── ToDoItem.jsx
├── services/
│   └── …
├── App.jsx
└── main.jsx
```

The test for *page* is simple: does a `<Route>` in `App.jsx` draw it? `Home` and `ListPage` are drawn by routes, and `AuthPage` is drawn in place of all of them. Everything else is a component.

## A component made of several files gets a folder of its own

`ToDoItem` is only ever drawn by `ToDoList`. Nobody else uses it. So the two go in a folder together, `components/ToDoList/`, and the folder says what the file names could not: these belong together, and `ToDoItem` is not meant for anyone else.

`AddForm` and `TextInput` are the opposite case. `AddForm` uses `TextInput`, but so could any form in the app, so `TextInput` stays at the top level of `components/`.

## A file has the name of the component it exports

`ToDoList.jsx` exports `ToDoList`. Always, in this course: one component per file, with the same name, so that searching for a component and opening its file are the same thing. A service file is named after the thing it handles, `listService.js`, and exports functions.

## Moving files is a refactoring too, so do it on a branch of its own

Moving `Home.jsx` into `pages/` changes every `import` that mentions it, and nothing else. That is a perfect pull request: easy to review, and easy to get wrong if it is mixed in with a new feature. Do it on its own branch, as in [Collaboration with Git Flow](../Tooling/Collaboration-with-Git-Flow.md), run the app, and merge.

Your editor helps: in VS Code, dragging a file to another folder in the sidebar offers to update the imports for you.

## No organisation is final

This is a structure to *start* from. When the app grows in a direction it did not foresee, say a dozen components that only the list page uses, give them a folder of their own and move them. You will not get it right the first time, and you do not need to: moving files is cheap, as long as you keep doing it.

## Exam Questions

### 1. How do you decide whether a component goes in `pages/` or in `components/`?

### 2. `ToDoItem` lives in a folder with `ToDoList`, but `TextInput` does not live in a folder with `AddForm`. Why?
