const loginForm = document.querySelector("#login-form");
const loginInput = loginForm.querySelector("input");
const loginButton = loginForm.querySelector("button");
const link = document.querySelector("a");

function onLoginSubmit(event) {
    // console.dir(loginInput);
    event.preventDefault(); // prevent refresh
    const userName = loginInput.value;
    console.log(userName);
    console.log(event);
}

function handleLinkClick(event) {
    console.log(event);
    alert("clicked");
}

loginForm.addEventListener("submit", onLoginSubmit);
link.addEventListener("click", handleLinkClick);