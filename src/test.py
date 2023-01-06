import random
import socket

# # Ouvrir un socket UDP
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
# # Spécifier l'adresse et le port sur lesquels envoyer les données
# sock.bind(('localhost', 6004))
#
# while True:
#     # Demander à l'utilisateur de saisir un message à envoyer
#     data, addr = sock.recvfrom(1024)
#     data = data.decode()
#     print("Données reçues du client {} : {}".format(addr, data))
#
# Serveur 1
import socket
from time import sleep

SERVER_ADDRESS = ("localhost", 6001)
MIDDLEWARE = ("localhost", 6002)
CLIENT_ADDRESS = ("localhost", 6000)
JEU_ADDRESS = ("localhost", 6004)
# Création du socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Liaison du socket à une adresse et un port
sock.bind(('localhost', 6004))

# Réception d'un message
message, address = sock.recvfrom(1024)
message = message.decode()
# Affichage du message reçu
print('Received message: {}'.format(message))


def motus(word, length):
    letters_to_guess = [False] * length
    tries_left = 6

    print(f"Le mot a {length} lettres.")

    a = f"Le mot a {length} lettres."
    print("Données envoyé au Middlewre {} : {}".format(MIDDLEWARE, a))
    sock.sendto(a.encode(), MIDDLEWARE)

    while True:
        # Réception d'un message
        check = False
        guess = None
        if check:
            message, address = sock.recvfrom(1024)
            message = message.decode()
            guess = message
        # Affichage du message reçu
        print('Received message depuis le middleware: {}'.format(message))

        if guess == word:
            print("Bien joué ! Le mot était", word + '.')
            b = "Bien joué ! Le mot était", word + '.'
            print("Données envoyé au Middlewre {} : {}".format(MIDDLEWARE, a))
            sock.sendto(b.encode(), MIDDLEWARE)
            return True
        else:
            tries_left -= 1
            print("Faux, vous avez encore : ", tries_left, "essais.")
            b = "Faux, vous avez encore : " + str(tries_left) + "essais."
            print("Données envoyé au Middlewre {} : {}".format(MIDDLEWARE, a))
            sock.sendto(b.encode(), MIDDLEWARE)
            # Check each letter in the guess
            if len(guess) == length:
                for i in range(length):
                    if guess[i] == word[i]:
                        letters_to_guess[i] = True

                # Print the letters that have been guessed correctly
                print("Lettres devinées :", end=' ')
                b = "Lettres devinées :".end
                print("Données envoyé au Middlewre {} : {}".format(MIDDLEWARE, a))
                sock.sendto(b.encode(), MIDDLEWARE)
                for i in range(length):
                    if letters_to_guess[i]:
                        print(word[i], end=' ')
                print()
            else:
                print("Le nombre de lettres de votre saisie est incorrect.")
                b = "Le nombre de lettres de votre saisie est incorrect."
                print("Données envoyé au Middlewre {} : {}".format(MIDDLEWARE, a))
                sock.sendto(b.encode(), MIDDLEWARE)
            if tries_left == 0:
                print("Game Over, le mot était :", word)
                b = "Game Over, le mot était : " + word
                print("Données envoyé au Middlewre {} : {}".format(MIDDLEWARE, a))
                sock.sendto(b.encode(), MIDDLEWARE)
                return False


word = format(message)
length = len(word)

motus(word, length)
