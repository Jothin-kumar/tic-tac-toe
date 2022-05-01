let currentChr = "X";
let XPoint = [];
let OPoint = [];
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
            if (currentChr === "X") {
                XPoint.push(this);
            } else {
                OPoint.push(this);
            }
            switchChr();
            checkWin();
        }
    }
}
function switchChr() {
    const statusLabel = document.getElementById("status");
    if (currentChr === "X") {
        currentChr = "O";
        statusLabel.innerText = "O's turn";
    } else {
        currentChr = "X";
        statusLabel.innerText = "X's turn";
    }
}
class winningPossibility {
    constructor(x1, y1, x2, y2, x3, y3) {
        this.x1 = x1;
        this.y1 = y1;
        this.x2 = x2;
        this.y2 = y2;
        this.x3 = x3;
        this.y3 = y3;
    }
}
function checkWinningPossibility(winningPossibility, forChr) {
    let p1Satisfied = false;
    let p2Satisfied = false;
    let p3Satisfied = false;
    if (forChr === 'X') {
        for (let i = 0; i < XPoint.length; i++) {
            if (XPoint[i].x === winningPossibility.x1 && XPoint[i].y === winningPossibility.y1) {
                p1Satisfied = true;
            }
            else if (XPoint[i].x === winningPossibility.x2 && XPoint[i].y === winningPossibility.y2) {
                p2Satisfied = true;
            }
            else if (XPoint[i].x === winningPossibility.x3 && XPoint[i].y === winningPossibility.y3) {
                p3Satisfied = true;
            }
        }
    } else {
        for (let i = 0; i < OPoint.length; i++) {
            if (OPoint[i].x === winningPossibility.x1 && OPoint[i].y === winningPossibility.y1) {
                p1Satisfied = true;
            }
            else if (OPoint[i].x === winningPossibility.x2 && OPoint[i].y === winningPossibility.y2) {
                p2Satisfied = true;
            }
            else if (OPoint[i].x === winningPossibility.x3 && OPoint[i].y === winningPossibility.y3) {
                p3Satisfied = true;
            }
        }
    }
    return p1Satisfied && p2Satisfied && p3Satisfied;
}
const winningPossibilities = [
    new winningPossibility(1, 1, 1, 2, 1, 3),
    new winningPossibility(2, 1, 2, 2, 2, 3),
    new winningPossibility(3, 1, 3, 2, 3, 3),
    new winningPossibility(1, 1, 2, 1, 3, 1),
    new winningPossibility(1, 2, 2, 2, 3, 2),
    new winningPossibility(1, 3, 2, 3, 3, 3),
    new winningPossibility(1, 1, 2, 2, 3, 3),
    new winningPossibility(3, 1, 2, 2, 1, 3)
]
function checkWin() {
    const statusLabel = document.getElementById("status");
    for (let i = 0; i < winningPossibilities.length; i++) {
        if (checkWinningPossibility(winningPossibilities[i], 'X')) {
            statusLabel.innerText = "X wins";
            disableGame();
            return;
        }
        if (checkWinningPossibility(winningPossibilities[i], 'O')) {
            statusLabel.innerText = "O wins";
            disableGame();
            return;
        }
    }
    if (XPoint.length + OPoint.length === 9) {
        statusLabel.innerText = "Draw";
        disableGame();
    }
}
function disableGame() {
    const buttons = document.getElementsByClassName("square");
    for (let i = 0; i < buttons.length; i++) {
        buttons[i].disabled = true;
    }
    const playAgainButton = document.getElementById("play-again");
    playAgainButton.style.display = "block";
}
function playAgain() {
    const buttons = document.getElementsByClassName("square");
    for (let i = 0; i < buttons.length; i++) {
        buttons[i].disabled = false;
        buttons[i].innerText = "";
    }
    XPoint = [];
    OPoint = [];
    currentChr = "X";
    const statusLabel = document.getElementById("status");
    statusLabel.innerText = "X's turn";
    const playAgainButton = document.getElementById("play-again");
    playAgainButton.style.display = "none";
}
function setup() {
    let squareElements = document.getElementsByClassName("square");
    for (let i = 0; i < squareElements.length; i++) {
        new XOSquare(i % 3 + 1, Math.floor(i / 3) + 1, squareElements[i].id);
    }
}
window.onload = setup;
let currentTheme = 'light';
function switchTheme() {
    if (currentTheme === 'dark') {
        document.querySelectorAll('.dark-mode').forEach(function (element) {
            element.classList.remove('dark-mode');
            element.classList.add('light-mode');
        });
        currentTheme = 'light';
    }
    else {
        document.querySelectorAll('.light-mode').forEach(function (element) {
            element.classList.remove('light-mode');
            element.classList.add('dark-mode');
        });
        currentTheme = 'dark';
    }
}
