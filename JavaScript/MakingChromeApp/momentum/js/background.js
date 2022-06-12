const images = [
    "0.jpeg",
    "1.jpeg",
    "2.jpeg"
];
const imageLength = images.length;

const chosenImage = images[Math.floor(Math.random() * imageLength)];

const bgImage = document.createElement("img");
bgImage.src = `img/${chosenImage}`;

// add the element to the body
document.body.appendChild(bgImage);