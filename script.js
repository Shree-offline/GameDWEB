let secretNumber = Math.floor(Math.random() * 100) + 1;

function checkGuess() {
    let guess = document.getElementById('guessInput').value;
    let feedback = document.getElementById('feedback');

    // Prevent empty guesses
    if (!guess) {
        feedback.innerText = "Please enter a number!";
        feedback.style.color = "#ffb84c"; // Orange
        return;
    }

    if (guess == secretNumber) {
        feedback.innerText = "🎉 You Won! 🎉";
        feedback.style.color = "#4cff88"; // Green
    } else if (guess > secretNumber) {
        feedback.innerText = "Too high! 📉";
        feedback.style.color = "#ff4c4c"; // Red
    } else {
        feedback.innerText = "Too low! 📈";
        feedback.style.color = "#4c8eff"; // Blue
    }
}
