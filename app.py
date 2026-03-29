import random

def play_game():
    print("🎮 Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            # Get the player's guess
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Check the guess against the secret number
            if guess < secret_number:
                print("Too low! Try a higher number. 📈")
            elif guess > secret_number:
                print("Too high! Try a lower number. 📉")
            else:
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempts!")
                break # Exit the loop because the player won
                
        except ValueError:
            # Handle the case where the user types letters instead of numbers
            print("Invalid input! Please enter a number.")

# Start the game
if __name__ == "__main__":
    play_game()
