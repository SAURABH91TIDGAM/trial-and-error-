$(document).ready(function() {
    let fragments = $(".fragment");
    let resetBtn = $("#reset-btn");
    let newGameBtn = $("#newgame-btn");
    let msgContainer = $(".message-container");
    let message = $("#message");
    let instructions = $("#instructions");

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
    ];

    $("#player1NameInput, #player2NameInput").on('blur', savePlayerNames);

    function savePlayerNames() {
        var player1Name = $("#player1NameInput").val();
        var player2Name = $("#player2NameInput").val();
        localStorage.setItem('player1Name', player1Name);
        localStorage.setItem('player2Name', player2Name);
    }

    fragments.on('click', function() {
        if (turn) {
            $(this).text("O");
            turn = false;
        } else {
            $(this).text("X");
            turn = true;
        }
        $(this).prop('disabled', true);
        count++;
        let isWinner = checkWinner();
        if (count === 9 && !isWinner) {
            gameDraw();
        }
    });

    const gameDraw = () => {
        message.text(`Game was a Draw.`);
        msgContainer.removeClass("hide");
        disableBoxes();
    };

    const disableBoxes = () => {
        fragments.prop('disabled', true);
    };

    const enableBoxes = () => {
        fragments.prop('disabled', false).text("");
    };

    const resetGame = function () {
        turn = true;
        count=0;
        enableBoxes();
        instructions.removeClass("hide");
        msgContainer.addClass("hide");
    };

    const showWinner = (winner) => {
        instructions.addClass("hide");
        let player1Name = localStorage.getItem('player1Name');
        let player2Name = localStorage.getItem('player2Name');
        let winnerName = winner === 'O' ? player1Name : player2Name;
        message.addClass('congratulations').text(`Congratulations, Winner is ${winnerName} playing with ${winner}`);
        msgContainer.removeClass("hide");
        disableBoxes();
    };

    const checkWinner = () => {
        for (let pattern of winPatterns) {
            let positionOneValue = fragments.eq(pattern[0]).text();
            let positionTwoValue = fragments.eq(pattern[1]).text();
            let positionThreeValue = fragments.eq(pattern[2]).text();
            if (positionOneValue !== "" && positionTwoValue !== "" && positionThreeValue !== "") {
                if (positionOneValue === positionTwoValue && positionTwoValue === positionThreeValue) {
                    showWinner(positionOneValue);
                    return true;
                }
            }
        }
        return false;
    };

    newGameBtn.on("click", resetGame);
    resetBtn.on("click", resetGame);
});
