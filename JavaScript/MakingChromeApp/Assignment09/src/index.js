const colors = [
    "#ef5777",
    "#575fcf",
    "#4bcffa",
    "#34e7e4",
    "#0be881",
    "#f53b57",
    "#3c40c6",
    "#0fbcf9",
    "#00d8d6",
    "#05c46b",
    "#ffc048",
    "#ffdd59",
    "#ff5e57",
    "#d2dae2",
    "#485460",
    "#ffa801",
    "#ffd32a",
    "#ff3f34"
  ];
const colorLen = colors.length;
const button = document.querySelector("button");
const body = document.querySelector("body");

function pickRandomColor(numSize) {
    const n1 = Math.floor(numSize * Math.random());
    const n2 = Math.floor((numSize-1) * Math.random());
    if (n2 < n1) { // n2 ... n1 ...
        return [colors[n1], colors[n2]];
    }
    else { // n1 ... n2 ...
        return [colors[n1], colors[n2+1]];
    }
}

function handleClick(event) {
    event.preventDefault();
    const pickedColors = pickRandomColor(colorLen);
    body.style.background = 'linear-gradient(90deg,' + pickedColors[0] + ',' + pickedColors[1] + ')';
}

button.addEventListener("click", handleClick);