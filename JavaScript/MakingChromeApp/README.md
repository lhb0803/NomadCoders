Lecture from NomadCoders: [link](https://nomadcoders.co/javascript-for-beginners)

# 1.1 What Are We Building
* Momentum App Clone Coding

# 1.2 Requirements
* HTML, CSS

# 1.3 Software Requirements
* Chromium Browser (ex. Chrome, Brave, Whale)
* VS Code

# 1.4 Why JS
1. History: created due to Netscape
2. Only Frontend Language
3. JS is already in Every machine (unlike Python)
4. Framework: React Native, Electron, socket.io
5. You can do A lot of things with JS: make a website, backend, chat, desktop app, machine learning

# 2 Welcome to JavaScript

# 3 Javascript on Browser
## 3.0 The Document Object
* A browser has a **document** object
* We can call HTML tag from JS environment through an access to document object
* We can change HTML data by changing document object's properties

## 3.1 HTML in Javascript
* Get things from document
* Change things from document

## 3.2 Searching for Elements
* `getElementsByClassName()`, `getElementsByTagName()`
* `querySelector()`, `querySelectorAll()`: can access through CSS notation (much better way)

## 3.3 Events
* `on...`: event related property
* Javascript can listen **events**
* `addEventListener("click", func)`: listen for 'click' event -> when click happens, do 'func'

## 3.4 Events Part two
* MDN: HTML Explanation -> So many things that can be detected

## 3.5 More Events
* Another way to handle events

## 3.6 CSS in Javascript
* if-else
* Ready to build app
    - step 1. get the element
    - step 2. listen to the event
    - step 3. react to the event

## 3.7 CSS in Javascript Part two
* Right tool for style is **CSS** (not JS): JS is appropriate for animation

## 3.8 CSS in Javascript Part three
* Fixing bug: not changing pre-existed class name

## 4.0 Input Values
* Start making App

## 4.1 Form Submission
* HTML helps us filling form
* But the form is submitted and the browser is refreshed

## 4.2 Events
* event function recieve an **argument**

## 4.3 Events part two
* Handling Other events like `MouseEvent` 
* `MouseEvent` shows X, Y coordinates
* Each event returns different information

## 4.4 Getting Username
* Hiding and Showing through CSS
* Combining string with backtick and $

## 4.5 Saving Username
* `localStorage` in Browser: `setItem(key, value)`, `removeItem(key)`
* Save the user name to `localStorage`

## 4.6 Loading Username
* Get user name from `localStorage`

## Assignment04
* [link](https://codesandbox.io/s/day-three-blueprint-forked-ztr0cr?file=/src/index.js)

## Assignment05
* [link](https://codesandbox.io/s/assignment05-qtj7yx)

## 5.0 Intervals
* divide source code in different file - code file per feature
* `setInterval(func, interval)`: repeat `func` every `interval`

## 5.1 Timeouts and Dates
* `setTimeout()`: wait
* `Date()`: `new Date()`

## 5.2 PadStart
* `"string".padStart(2,"0")`

## 6.0 Quotes
* Randomness by `Math` module
* `Math.round()`, `Math.ceil()`, `Math.floor()`: make a float an integer

## 6.1 Background
* Create element from JS
    * `document.createElement("img")`
* Add the element to the body
    * `document.body.appendChild(bgImage)`

## 7.0 Setup
* Todos

## 7.1 Adding ToDos
* Create list (`<li>`)
* Add `<span>` to `<li>` by `li.appendChild()`
* Problem: cannot delete or save list

## 7.2 Deleting ToDos
* Button should listen click event
* `event` argument shows **which button is clicked**
    * `event.path`, `event.target`, `event.target.parentElement`
    * `console.dir(event.target)`: shows button's property

## 7.3 Saving ToDos
* `localStorage`: save to the browser
* `localStorage` **cannot save array** ; only text can be saved
    * `JSON.stringify(object)`: turns object to string

## 7.4 Loading ToDos part One
* How to Show on window
* `JSON.parse(String)`: turns string to object
* `forEach(func)`: each element goes into `func`'s argument

## 7.5 Loading ToDos part Two
* How to restore instead of overwriting
* update JS array to `localStorage`'s array

## 7.6 Deleting ToDos part One
* Give toDos an **id**
* Make toDos as array of **Object**s
* `Date.now()` gives miliseconds -> use it as an **id**
* Can delete with the **id**