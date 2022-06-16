const upperLimitForm = document.querySelector("#upper-limit")
const upperLimitValue = upperLimitForm.querySelector("input");

const guessingForm = document.querySelector("#guessing");
const guessingValue = guessingForm.querySelector("input");

let upperLimit = 0;
let guessingNum = 0;

const matching = document.querySelector("#matching");
const result = document.querySelector("#result");

function printMatchResult(machineNum, text) {
    matching.innerText = `You chose: ${guessingNum}, the machine chose: ${machineNum}.`
    matching.classList.remove("hidden");

    result.innerHTML = `<b>${text}</b>`;
    result.classList.remove("hidden");
}

function handleUpperLimitSubmit(event) {
    event.preventDefault();
    upperLimit = upperLimitValue.value;
}

function alertUpperLimit() {
    const warningText = `${guessingNum} is larger than ${upperLimit}`
    printMatchResult(null, warningText);
}

function match() {
    const machineNum = Math.round(Math.random() * upperLimit)
    if (machineNum == guessingNum) {
        printMatchResult(machineNum, "You win!");
    }
    else {
        printMatchResult(machineNum, "You lost!");
    }
}

function handleGuessing(event) {
    event.preventDefault();
    guessingNum = guessingValue.value;

    if (guessingNum > upperLimit) {
        alertUpperLimit();
    }
    else {
        match();
    }
}

upperLimitForm.addEventListener("submit", handleUpperLimitSubmit);
guessingForm.addEventListener("submit", handleGuessing);
