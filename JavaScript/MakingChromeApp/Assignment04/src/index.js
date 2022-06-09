// <⚠️ DONT DELETE THIS ⚠️>
import "./styles.css";
const colors = ["#1abc9c", "#3498db", "#9b59b6", "#f39c12", "#e74c3c"];
// <⚠️ /DONT DELETE THIS ⚠️>

/*
✅ The text of the title should change when the mouse is on top of it.
✅ The text of the title should change when the mouse is leaves it.
✅ When the window is resized the title should change.
✅ On right click the title should also change.
✅ The colors of the title should come from a color from the colors array.
✅ DO NOT CHANGE .css, or .html files.
✅ ALL function handlers should be INSIDE of "superEventHandler"
*/

const superEventHandler = {
    handleMouseOver: function() {
        h2.className = "mouseover";
        h2.innerText = "The mouse is here!";
        h2.style.color = colors[0];
    },
    handleMouseLeave: function() {
        h2.className = "mouseleave";
        h2.innerText = "The mouse is gone!";
        h2.style.color = colors[1];
    },
    handleResize: function() {
        h2.className = "resize";
        h2.innerText = "You just resized";
        h2.style.color = colors[2];
    },
    handleRightClick: function() {
        h2.className = "rightClick";
        h2.innerText = "That was a right click!";
        h2.style.color = colors[3];
    }
};
const h2 = document.querySelector("h2");

h2.addEventListener("mouseover", superEventHandler.handleMouseOver);
h2.addEventListener("mouseleave", superEventHandler.handleMouseLeave);
window.addEventListener("resize", superEventHandler.handleResize);
window.addEventListener("contextmenu", superEventHandler.handleRightClick);