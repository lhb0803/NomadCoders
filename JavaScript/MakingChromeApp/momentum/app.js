const title = document.getElementById("title");

function handleTitleClick() {
    console.log("title was clicked");
    title.style.color = "blue";
}

title.addEventListener("click", handleTitleClick);