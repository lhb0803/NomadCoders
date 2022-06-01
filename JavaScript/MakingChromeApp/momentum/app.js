const h1 = document.getElementById("title");

function handleTitleClick() {
    const clickedClass = "clicked"
    if (h1.className === clickedClass) {
        h1.className = "";
    }
    else {
        h1.className = clickedClass;
    }
}

h1.onclick = handleTitleClick;
