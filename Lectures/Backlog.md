

- Access Control - not essential? 

- What do we save in LocalStorage and what do we save in the DB? 




## Single Page Application Architecture

![](images/spa-architecture.png)





Advanced DB topics
	- [Live Queries](https://www.back4app.com/docs/react/real-time/react-hook-real-time)
		- how to get notified when data changes 


### A bit about APIs
- https://rickandmortyapi.com/ 
- you can see by example:
	- REST
	- GraphQL
- you test them with Postman
- you also test them with the help of the `fetch` API


## Advanced Questions / To Think About

1. What happens when one sends a full url straight to the server? e.g. zeeguu.org/exercises? 


# Single Page Applications

#### What are Single Page Applications (SPAs)? 

#### Why are they useful? 

#### What's the relationship between the client-server architecture and SPAs?



#### How to protect some routes if the user is not loggedIn? 




Git
- what do you not commit to git?
- what is a fork? 




**From the React Tutorial**
Managing State (subsections)
- Choosing the State Structure (Principles for structuring state)
- Sharing State Between Components
- Preserving and resetting state (quite detailed about component state lifetime)
- Extracting state logic into a reducer (command pattern)
- Passing data deeply with context

Escape Hatches (subsections)
- useRef
- manipulating the DOM with Refs
- Synchronizing with Effects





- [Forwarding props with the spread syntax](https://react.dev/learn/passing-props-to-a-component#forwarding-props-with-the-jsx-spread-syntax)
- [Passing JSX as children](https://react.dev/learn/passing-props-to-a-component#passing-jsx-as-children)


See the example from: [Sharing data between components](https://react.dev/learn#sharing-data-between-components)
- moving the state up is also calling *lifting the state*

Advanced: A special kind of prop is the `children` prop that, when used inside of a component definition refers to the JSX contained in the component. [Read and see example](https://react.dev/learn/passing-props-to-a-component#passing-jsx-as-children)

Hooks



- Reactive programming - as opposed to declarative programming
	- [Reacting to Input with State](https://react.dev/learn/reacting-to-input-with-state) (from react.dev)




- [Updating Objects in State](https://react.dev/learn/updating-objects-in-state)
- [Updating Arrays in State](https://react.dev/learn/updating-arrays-in-state)

- UI Patterns
	- Rendering a list of elements 



## Designing with Components

One possible process: 
- Breaking the UI in a component hierarchy
- 


Fundamental React: when a prop is changed, the component is also redrawn (reactive programming). See the [clock example](https://react.dev/learn/passing-props-to-a-component#how-props-change-over-time). 
