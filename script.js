let currentChr = "X";
class XOSquare {
    constructor(x, y, buttonId) {
        this.x = x;
        this.y = y;
        this.button = document.getElementById(buttonId);
        this.button.onclick = () => {
            this.set(buttonId)
        }
    }
    set(buttonId) {
        this.button = document.getElementById(buttonId);
        if (this.button.innerText === "") {
            this.button.innerText = currentChr;
            switchChr();
        }
    }
    reset() {
        this.button.innerText = "";
    }
}
function switchChr() {
    if (currentChr === "X") {
        currentChr = "O";
    } else {
        currentChr = "X";
    }
}
function setup() {
    let squares = [];
    let squareElements = document.getElementsByClassName("square");
    for (let i = 0; i < squareElements.length; i++) {
        let square = new XOSquare(i % 3, Math.floor(i / 3), squareElements[i].id);
        squares.push(square);
    }
}
window.onload = setup;
