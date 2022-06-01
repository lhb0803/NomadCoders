const title = document.getElementById("title");

function handleTitleClick() {
    console.log("title was clicked");
    title.style.color = "blue";
}

function handleMouseEnter() {
    console.log("mouse is here!");
    title.innerText = "Mouse is here!"
}

function handleMouseLeave() {
    title.innerText = "Mouse is gone!"
}

title.addEventListener("click", handleTitleClick);
title.addEventListener("mouseenter", handleMouseEnter);
title.addEventListener("mouseleave", handleMouseLeave);