import random


def motus(word, length):
    letters_to_guess = [False] * length
    tries_left = 6

    # Print the number of letters in the word
    print(f"Le mot a {length} lettres.")

    while True:
        guess = input("Devinez le mot : ")
        if guess == word:
            print("Bien joué ! Le mot était", word + '.')
            return True
        else:
            tries_left -= 1
            print("Faux, vous avez encore : ", tries_left, "essais.")

            if tries_left == 0:
                print("Game Over, le mot était :", word)
                return False


words = ["frustant", "terrible", "baignoire", "developpeur"]
word = random.choice(words)
length = len(word)
motus(word, length)
