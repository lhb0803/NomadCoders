const loginForm = document.querySelector("#login-form");
const loginInput = loginForm.querySelector("input");
const loginButton = loginForm.querySelector("button");

function onLoginSubmit(event) {
    // console.dir(loginInput);
    event.preventDefault(); // prevent refresh
    const userName = loginInput.value;
    console.log(userName);
    console.log(event);
}

loginForm.addEventListener("submit", onLoginSubmit);