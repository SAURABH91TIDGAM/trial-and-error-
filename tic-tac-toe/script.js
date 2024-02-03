let fragments = document.querySelectorAll(".fragment");
let resetBtn = document.querySelector("#reset-btn");
let newGameBtn = document.querySelector("#newgame-btn");
let msgContainer = document.querySelector(".message-container");
let message = document.querySelector("#message");
let instructions = document.querySelector("#instructions");

let turn = true; //playerX, playerO
let count = 0; //To Track Draw

const winPatterns = [
    [0, 1, 2],
    [0, 3, 6],
    [0, 4, 8],
    [1, 4, 7],
    [2, 5, 8],
    [2, 4, 6],
    [3, 4, 5], 
    [6, 7, 8],
]

fragments.forEach((fragment) => {
    fragment.addEventListener('click', () => {
        console.log("box was clicked");
        if (turn) {
            //playerO
            fragment.innerText = "O";
            turn = false;
        }
        else {
            //playerX
            fragment.innerText = "X";
            turn = true;
        }
        fragment.disabled = true;
        count++;
        let isWinner = checkWinner();
        
        console.log(count);
        if (count === 9 && !isWinner) {
            gameDraw();
        }
    });

    const gameDraw = () => {
        message.innerText = `Game was a Draw.`;
        msgContainer.classList.remove("hide");
        disableBoxes();
    };

    const disableFragments = () => {
        for (let fragment of fragments) {
            fragment.disabled = true;
        }
    };

    const enableFragments = () => {
        for (let fragment of fragments) {
            fragment.disabled = false;
            fragment.innerText = "";
        }
    };

    
    const resetGame = function () {
        turn = true;
        count=0;
        enableFragments();
        instructions.classList.remove("hide");
        msgContainer.classList.add("hide");
    };

    const showWinner = (winner) => {
        instructions.classList.add("hide");
        if (winner === 'O') {
            message.innerText = `Congratulations, Winner is Player One playing with ${winner}`;
            msgContainer.classList.remove("hide");
            
            disableFragments();
        }
        else if (winner === 'X') {
            message.innerText = `Congratulations, Winner is Player Two playing with ${winner}`;
            msgContainer.classList.remove("hide");
            disableFragments();
        }
        else if (winner === ""){
            message.innerText = `It's a draw`;
            msgContainer.classList.remove("hide");
            disableFragments();
        }
     }


    const checkWinner = () => {
        for (let pattern of winPatterns) {
            // console.log(pattern[0], pattern[1], pattern[2]);
            // console.log(fragments[pattern[0]], fragments[pattern[1]], fragments[pattern[2]]);
            // console.log(fragments[pattern[0]].innerText, fragments[pattern[1]].innerText, fragments[pattern[2]].innerText);

            let positionOneValue = fragments[pattern[0]].innerText;
            let positionTwoValue = fragments[pattern[1]].innerText;
            let positionThreeValue = fragments[pattern[2]].innerText;

            if (positionOneValue != "" && positionTwoValue != "" && positionThreeValue != "") {
                if (positionOneValue === positionTwoValue && positionTwoValue === positionThreeValue) {
                    showWinner(positionOneValue);
                }
            }
        }
    };

    newGameBtn.addEventListener("click", resetGame);
    resetBtn.addEventListener("click", resetGame);



});