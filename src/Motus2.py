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

SERVER_ADDRESS = ("localhost", 6001)
MIDDLEWARE = ("localhost", 6002)
CLIENT_ADDRESS = ("localhost", 6000)
JEU_ADDRESS = ("localhost", 6004)
# Création du socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Liaison du socket à une adresse et un port
sock.bind(('localhost', 6004))

def enlever_doublons(liste):
    # Créer une liste vide
    liste_sans_doublons = []
    # Parcourir chaque élément de la liste
    for i in liste:
        # Si l'élément n'est pas déjà dans la liste temporaire, l'ajouter
        if i not in liste_sans_doublons:
            liste_sans_doublons.append(i)
    # Retourner la liste temporaire
    return liste_sans_doublons
def motus(liste, mot, taille, vie, i):
    # Sélectionnez un mot aléatoire de la liste de mots
    communes = []
    liste = liste[i]
    print(liste)
    # Vérifiez si le mot sélectionné a la même longueur que le mot cible
    if len(liste) != len(mot):
        a = "Le mot sélectionné n'a pas la même longueur que le mot cible"
        print("Données envoyé au Middlewre {} : {}".format(MIDDLEWARE, a))
        sock.sendto(a.encode(), MIDDLEWARE)


    # Initialisez un compteur de bonnes lettres à 0
    else:
        good_letters = 0
        # Répétez le processus jusqu'à ce que le mot cible soit deviné ou que les vies soient épuisées
        if good_letters < taille and vie > 0:
            # Demandez à l'utilisateur de deviner une lettre
            guess = liste
            print('guess:' +guess)
            # Vérifiez si la lettre devinée se trouve dans le mot cible
            for lettre in guess:
                if lettre in mot:
                    # Si oui, augmentez le compteur de bonnes lettres
                    good_letters += 1
                    communes.append(lettre)
                    communes = enlever_doublons(communes)
                    print(communes)


            # Vérifiez si le mot cible a été deviné
            print(good_letters)
            print(taille)
            if good_letters == taille:
                if liste == mot:
                    b = ("Vous avez gagné !")
                    print("Données envoyé au Middlewre {} : {}".format(MIDDLEWARE, b))
                    sock.sendto(b.encode(), MIDDLEWARE)
                else:
                    c = "Essayez encore, lettres corrects : " + str(communes) + '\n vie restantes : ' + str(vie)
                    print("Données envoyé au Middlewre {} : {}".format(MIDDLEWARE, c))
                    sock.sendto(c.encode(), MIDDLEWARE)
            else:
                c = "Essayez encore, lettres corrects : " + str(communes) + '\n vie restantes : ' + str(vie)
                print("Données envoyé au Middlewre {} : {}".format(MIDDLEWARE, c))
                sock.sendto(c.encode(), MIDDLEWARE)



# Réception d'un message
message, address = sock.recvfrom(1024)
message = message.decode()
# Affichage du message reçu
print('Received message: {}'.format(message))
mot = message
liste = []
vie = 6
taille = len(mot)
b = str(taille) + ' voici la taille du mot'
print("Données envoyé au Middlewre {} : {}".format(MIDDLEWARE, b))
sock.sendto(b.encode(), MIDDLEWARE)
for i in range(taille):
    message, address = sock.recvfrom(1024)
    message = message.decode()
    # Affichage du message reçu
    print('Received message: {}'.format(message))
    liste.append(message)
    motus(liste, mot, taille, vie, i)
    vie -= 1
    print(vie)


# def motus(word, length):
#     letters_to_guess = [False] * length
#     tries_left = 6
#
#     print(f"Le mot a {length} lettres.")
#
#     a = f"Le mot a {length} lettres."
#     print("Données envoyé au Middlewre {} : {}".format(MIDDLEWARE, a))
#     sock.sendto(a.encode(), MIDDLEWARE)
#
#     for i in range(taille):
#         guess = message
#         if guess == word:
#             print("Bien joué ! Le mot était", word + '.')
#             b = "Bien joué ! Le mot était", word + '.'
#             print("Données envoyé au Middlewre {} : {}".format(MIDDLEWARE, a))
#             sock.sendto(b.encode(), MIDDLEWARE)
#             return False
#         else:
#             tries_left -= 1
#             print("Faux, vous avez encore : ", tries_left, "essais.")
#             b = "Faux, vous avez encore : " + str(tries_left) + "essais."
#             print("Données envoyé au Middlewre {} : {}".format(MIDDLEWARE, a))
#             sock.sendto(b.encode(), MIDDLEWARE)
#             # Check each letter in the guess
#             if len(guess) == length:
#                 for i in range(length):
#                     if guess[i] == word[i]:
#                         letters_to_guess[i] = True
#
#                 # Print the letters that have been guessed correctly
#                 print("Lettres devinées :", end=' ')
#                 b = "Lettres devinées :".end
#                 print("Données envoyé au Middlewre {} : {}".format(MIDDLEWARE, a))
#                 sock.sendto(b.encode(), MIDDLEWARE)
#                 for i in range(length):
#                     if letters_to_guess[i]:
#                         print(word[i], end=' ')
#                     return False
#
#             else:
#                 print("Le nombre de lettres de votre saisie est incorrect.")
#                 b = "Le nombre de lettres de votre saisie est incorrect."
#                 print("Données envoyé au Middlewre {} : {}".format(MIDDLEWARE, a))
#                 sock.sendto(b.encode(), MIDDLEWARE)
#                 return False
#             if tries_left == 0:
#                 print("Game Over, le mot était :", word)
#                 b = "Game Over, le mot était : " + word
#                 print("Données envoyé au Middlewre {} : {}".format(MIDDLEWARE, a))
#                 sock.sendto(b.encode(), MIDDLEWARE)
#                 return False
#
#
# word = format(message)
# length = len(word)
#
# motus(word, length)
