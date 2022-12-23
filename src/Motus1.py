word = "apple"  #Mot secret

lives = 5
progress = "_" * len(word)

while lives > 0:
    # Print le jeu
    print(f"Progress: {progress}")
    print(f"Lives: {lives}")

    # Lecture des input du joueur
    guess = input("Donner un lettre: ")
    if len(guess) != 1:
        print("Invalide, il faut n'entrez qu'une seule lettre")
        continue

    # Mettre à jour le jeu selon les input du joueur
    if guess not in word:
        lives -= 1
        print("Faux! La lettre n'est pas dans le mot.")
    else:
        for i in range(len(word)):
            if word[i] == guess:
                progress = progress[:i] + guess + progress[i + 1:]

    # Vérifier si le joueur a gagné ou perdu
    if progress == word:
        print("Bien joué ! Vous avez deviné le mot : " + word)
        break
if lives == 0:
    print("Game over. Le mot était : " + word)




