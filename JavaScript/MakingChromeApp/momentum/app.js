const h1 = document.getElementById("title");

function handleTitleClick() {
    console.log("title was clicked");
    const currentColor = h1.style.color;
    let newColor;
    if (currentColor === "blue") {
        newColor = "tomato";
    }
    else {
        newColor = "blue";
    }
    h1.style.color = newColor;
}

h1.onclick = handleTitleClick;
