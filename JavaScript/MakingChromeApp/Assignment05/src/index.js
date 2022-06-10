let windowSize = window.innerWidth;
const smallWidth = 500;
const mediumWidth = 700;

const body = document.body;

const SMALL_WIDTH = "smallWidth";
const MEDIUM_WIDTH = "mediumWidth";
const LARGE_WIDTH = "largeWidth";

function setBackgroundColor(windowSize) {
    if (windowSize <= smallWidth) {
        body.classList.remove(MEDIUM_WIDTH);
        body.classList.add(SMALL_WIDTH);
    } 
    else if (windowSize <= mediumWidth) {
        body.classList.remove(SMALL_WIDTH);
        body.classList.remove(LARGE_WIDTH);
        body.classList.add(MEDIUM_WIDTH);
    }
    else {
        body.classList.remove(MEDIUM_WIDTH);
        body.classList.add(LARGE_WIDTH);
    }
}

function resizeHandler() {
    windowSize = window.innerWidth;
    setBackgroundColor(windowSize);
}

setBackgroundColor(windowSize);
window.addEventListener("resize", resizeHandler);
