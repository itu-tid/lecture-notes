
# React

React is a JavaScript **library** for building interactive user interfaces.


## Components

React is a *component-based* UI library. 

Every UI element in React is either a component or is composed of nested components.

Components are 
- (conceptually) reusable UI elements
- (technically) functions that return markup

Components are nested all the way down:
	- From small, e.g. buttons, to large, e.g. full web page or mobile screens

Conventions: 
- (naming) components are named with capital letters 
- (modularization): components are defined in their own files
- (modularization) To import a component one can use either *default* or *named* imports

[Example](https://react.dev/learn/your-first-component#defining-a-component) of a React component 




## JSX

JSX is 
- A markup syntax used in React to ease definition of UIs
- A combination of JS and HTML
- A stricter syntax than HTML
	- A component can [only ever return a single JSX tag](https://react.dev/learn/writing-markup-with-jsx#1-return-a-single-root-element) 
	- Tags must [always be closed](https://react.dev/learn/writing-markup-with-jsx#2-close-all-the-tags) 

JSX converts [most HTML and CSS attributes to camelCase](https://react.dev/learn/writing-markup-with-jsx#3-camelcase-salls-most-of-the-things) 
- `onclick` => `onClick`
- `background-color` => `backgroundColor`

Notes: 
- Similar approaches for other front-end JS frameworks (e.g., [Vue templates](https://www.freecodecamp.org/news/reacts-jsx-vs-vue-s-templates-a-showdown-on-the-front-end-b00a70470409/)) and server-side rendering frameworks (e.g. Jinja for Flask).
- JSX is transpiled to Javascript 






## Interpolating JS in JSX

Curly brackets to escape JS inside JSX can be used in three ways

1. As **text inside a component**

```
return (
  <>
    <h1>{"Hello" + user.firstName + user.LastName}</h1>
    <p>Today is: {todaysDate}</p>
  </>
);
```

2. As **attributes immediately following the `=` sign**
```
return (
  <img
    className="avatar"
    src={user.imageUrl}
  />
);

```

3. Special case of attributes: **[double curlies](https://react.dev/learn/javascript-in-jsx-with-curly-braces#using-double-curlies-css-and-other-objects-in-jsx) for objects**
```
export default function TodoList() {
  return (
    <ul style={{
      backgroundColor: 'black',
      color: 'pink'
    }}>
      <li>Improve the videophone</li>
      <li>Prepare aeronautics lectures</li>
      <li>Work on the alcohol-fuelled engine</li>
    </ul>
  );
}

```






## Styling

CSS Styles can be defined 
- in a separate file, or 
- inline as the example above
- as local variables, as they use in React Native (e.g. [here](https://github.com/mircealungu/zeeguu-mobile/blob/master/screens/AllArticles.js))
- with the help of 3rd party libraries (we'll see later)

Warning: Use `className` instead of class (e.g. `<img className="avatar" />`) because `class` is reserved keyword in JS. 







## Conditional Rendering 

Often components need to display differently based on some state or prop. 

Three possible ways to render conditionally: 
1. If statements
1. The `conditional ? operator` 
1. When only one option is possible `logical && syntax` 

Note: 
- you can [conditionally return null](https://react.dev/learn/conditional-rendering#conditionally-returning-nothing-with-null) if you don't want to display a given component in some situation. 

Read and see examples at: *Describing the UI > [Conditional Rendering](https://react.dev/learn/conditional-rendering)*






## Rendering Lists

Most applications sooner or later rely on lists of things that you want to process. 

In React, to render lists: 
- You rely on `for` loops and  `array.map()`
- You must use a `key` attribute for every element in a list
	- must be unique
	- can be the database ID, UUID, or anything else unique
	- important internally for React's rendering

Nice examples of rendering lists and filtering at: *Describing the UI* > [Rendering Lists](https://react.dev/learn/rendering-lists). Also nice exercises at the bottom of the page.






## Parameterizing Components

A component is a drawing function + functions can be parameterized => Components  should be parameterizable

Component parameters are called **props** in React. 

How do component with props work? 
- In the moment when the *props* are [passed to the component](https://react.dev/learn/passing-props-to-a-component#step-1-pass-props-to-the-child-component), they *look* like HTML attributes -- have the same syntax
- In the component definition the props are accessed as a single function parameter named `props`. The props can be [destructured](https://react.dev/learn/passing-props-to-a-component#step-2-read-props-inside-the-child-component) using destructuring syntax.






## Responding to Events

Interactive apps must handle events: click, type, mouse move, screen touch, etc. 

Built-in components (e.g. `<button>`) support built-in events (e.g. `onClick`, etc.).

Associating event handlers with events is done with the attribute in curly brackets syntax, as above. (See [onClick example](https://react.dev/learn/responding-to-events#adding-event-handlers).)

Event handlers
- are defined inside components
- have usually names starting with `handle`... 

WARNING: Make sure to not call the function, but rather, pass it as a parameter! 


**Event handlers always receive an event as argument**, detailing info about what just happened. 
- Sometimes you can ignore it, 
- Sometimes you can inspect it to learn about the event (e.g. mouse position, element that was clicked, etc. )
- Sometimes you can change the behavior of the event by calling `stopPropagation` or `preventDefault` on the event object. [example of stop propagation](https://react.dev/learn/responding-to-events#stopping-propagation) and of [preventing default behavior](https://react.dev/learn/responding-to-events#preventing-default-behavior). 


Not Important: Events propagate (*bubble up*) the DOM tree. If you have an `onClick` handler on both a button and a containing div, both will be handled in sequence, from the inner one outwards. [See event propagation example](https://react.dev/learn/responding-to-events#event-propagation). 





## Component State

A component might need to store local state -- that might change (unlike props!).

In React, state is: 
- hidden inside each component 
- defined with `useState` that is 
	- a function defined in the `react` package, which
		- takes an **initial** value
		- returns **current value** and a **setter function**
		- is called a *hook* -- a special class of function in React

See the [button with counter example](https://react.dev/learn#updating-the-screen) for a combination of state and events






## Reactive Programming 

When a state variable defined with `useState` changes with the help of the setter (and thus, not changing the variable directly!!) a redrawing of the whole component is triggered. 

This is *reactive programming*. And reactive programming is why React is called so. 

A bit like in Excel -- one of the classical reactive programming environments -- where when you change one cell, all the others who depend on it and only those are changed automatically. 

In React, the dependents are not formulas, but UIs. When a state variable or a prop changes, the library automatically redraws all the relevant UI elements, and only those. 






## Connecting Inputs To State Via Event Handlers

The strange story of how you connect a state variable to the content of an input control in React: 

```
import { useState } from 'react';

export default function InputExample () {
  const [answer, setAnswer] = useState('');

  async function handleSubmit(e) {
    e.preventDefault();
    // do something with the answer 
    // ... 
  }

  function handleTextareaChange(e) {
    setAnswer(e.target.value);
  }

  return (
    <>
  
	  <form onSubmit={handleSubmit}>

		<textarea
          value={answer}
          onChange={handleTextareaChange}
          disabled={status === 'submitting'}
        />
        <br />
        
        <button disabled={answer.length === 0}>
          Submit
        </button>
      
      </form>
    </>
  );
}
```







# References

Read up from the [react.dev](https://react.dev) documentation site, the following: 

- Describing the UI
	- [Importing and Exporting Components](https://react.dev/learn/importing-and-exporting-components)
	- [Writing Markup with JSX](https://react.dev/learn/writing-markup-with-jsx)
	- [JS in JSX](https://react.dev/learn/javascript-in-jsx-with-curly-braces)
	- [Passing Props](https://react.dev/learn/passing-props-to-a-component)
	- [Conditional Rendering](https://react.dev/learn/conditional-rendering)
	- [Rendering Lists](https://react.dev/learn/rendering-lists)

- Adding Interactivity
	- [Responding to Events](https://react.dev/learn/responding-to-events) 
	- [State: A Component's Memory](https://react.dev/learn/state-a-components-memory)














