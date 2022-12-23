WORD = "apple"  # The secret word

# Initialize the game state
lives = 5
progress = "_" * len(WORD)

while lives > 0:
    # Print the game state
    print(f"Progress: {progress}")
    print(f"Lives: {lives}")

    # Read the player's guess
    guess = input("Guess a letter: ")
    if len(guess) != 1:
        print("Invalid input. Please enter a single letter.")
        continue

    # Update the game state based on the player's guess
    if guess not in WORD:
        lives -= 1
        print("Wrong! The letter is not in the word.")
    else:
        for i in range(len(WORD)):
            if WORD[i] == guess:
                progress = progress[:i] + guess + progress[i+1:]

    # Check if the player has won or lost
    if progress == WORD:
        print("Congratulations! You have guessed the word: " + WORD)
        break
if lives == 0:
    print("Game over. The word was: " + WORD)
