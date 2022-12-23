WORD = "apple"  # The secret word

# Initialize the game state
lives = 5
progress = "_" * len(WORD)

while lives > 0:
    # Print le jeu
    print(f"Progress: {progress}")
    print(f"Lives: {lives}")

    # Lecture des input du joueur
    guess = input("Donner un lettre: ")
    if len(guess) != 1:
        print("Invalide, n'entrez qu'une seule lettre")
        continue

    # Mettre à jour le jeu selon les input du joueur
    if guess not in WORD:
        lives -= 1
        print("Faux! La lettre n'est pas dans le mot.")
    else:
        for i in range(len(WORD)):
            if WORD[i] == guess:
                progress = progress[:i] + guess + progress[i + 1:]

    # Vérifier si le joueur a gagné ou perdu
    if progress == WORD:
        print("Bien joué ! Vous avez deviné le mot : " + WORD)
        break
if lives == 0:
    print("Game over. Le mot était : " + WORD)
