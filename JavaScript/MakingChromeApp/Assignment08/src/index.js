const clockTitle = document.querySelector(".js-clock");
const presentYear = new Date().getFullYear();
const christmas = new Date(presentYear, 11, 25);

function getTimer() {
    const presentDate = new Date();
    const days = String(Math.floor((christmas.getTime() - presentDate.getTime()) / (1000 * 3600 * 24))).padStart(3, "0");
    const hours = String(Math.floor((christmas.getTime() - presentDate.getTime()) / (1000 * 3600)) - days*24).padStart(2, "0");
    const minutes = String(Math.floor((christmas.getTime() - presentDate.getTime()) / (1000 * 60)) - days*24*60 - hours*60).padStart(2, "0");
    const seconds = String(Math.floor((christmas.getTime() - presentDate.getTime()) / (1000)) - days*24*60*60 - hours*60*60 - minutes*60).padStart(2, "0");
    clockTitle.innerText = `${days}d ${hours}h ${minutes}m ${seconds}s`;
}

console.log(christmas);
getTimer();
setInterval(getTimer, 1000);