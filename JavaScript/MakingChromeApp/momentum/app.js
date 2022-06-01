const h1 = document.getElementById("title");

function handleTitleClick() {
    const clickedClass = "clicked"
    // if (h1.classList.contains(clickedClass)) {
    //     h1.classList.remove(clickedClass);
    // }
    // else {
    //     h1.classList.add(clickedClass);
    // }

    // https://developer.mozilla.org/en-US/docs/Web/API/DOMTokenList/toggle
    h1.classList.toggle(clickedClass); // like a switch button
}

h1.onclick = handleTitleClick;
