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

  var player1NameInput = document.getElementById('player1NameInput');
  var player2NameInput = document.getElementById('player2NameInput');

  // Add event listeners to capture input changes
  player1NameInput.addEventListener('blur', savePlayerNames);
  player2NameInput.addEventListener('blur', savePlayerNames);

  function savePlayerNames() {
    // Get player names from input fields
    var player1Name = player1NameInput.value;
    var player2Name = player2NameInput.value;

    // Store player names in local storage
    localStorage.setItem('player1Name', player1Name);
    localStorage.setItem('player2Name', player2Name);
}


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
            message.classList.add('congratulations');
            message.innerText = `Congratulations, Winner is Player One ${localStorage.player1Name} playing with ${winner}`;
            msgContainer.classList.remove("hide");
            
            disableFragments();
        }
        else if (winner === 'X') {
            message.classList.add('congratulations');
            message.innerText = `Congratulations, Winner is Player Two ${localStorage.player2Name} playing with ${winner}`;
            msgContainer.classList.remove("hide");
            disableFragments();
        }

        
     }


    const checkWinner = () => {
        for (let pattern of winPatterns) {

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