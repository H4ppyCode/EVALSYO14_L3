# import random
# import socket
# import urllib.request
#
# HOST, PORT = "localhost", 5000
#
# # Créez un socket en mode UDP
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
# # Liez le socket à l'adresse et au port donnés
# sock.bind((HOST, PORT))
#
# # Lisez les mots du fichier "motsfrgut.txt" depuis le lien donné et créez une liste de mots
# with urllib.request.urlopen("https://karczmarczuk.users.greyc.fr/TEACH/TAL/Textes/motsfrgut.txt") as f:
#     words = f.read().decode(encoding="iso-8859-1").split()
#
# while True:
#     # Recevez des données envoyées par le client
#     data, addr = sock.recvfrom(1024)
#     data = data.decode()
#     print("Données reçues de {} : {}".format(addr, data))
#
#     # Si le client envoie la commande "start game", envoyez un mot aléatoire au client
#
#     word = random.choice(words)
#     sock.sendto(word.encode(), addr)
import random
import socket
import urllib
import urllib.request
import socket
from random import choice

# Adresse et port du middleware
MIDDLEWARE_ADDRESS = ("localhost", 5001)

# Créez un socket en mode UDP

server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Liez le socket à l'adresse et au port du serveur
server_sock.bind(("localhost", 5000))

while True:
    # Recevez des données envoyées par le middleware

    data, addr = server_sock.recvfrom(1024)
    data = data.decode()
    print("Données reçues du middleware {} : {}".format(addr, data))

    # Si la commande est "start game", envoyez un mot aléatoire au client
    if data == "start game":
        with urllib.request.urlopen("https://karczmarczuk.users.greyc.fr/TEACH/TAL/Textes/motsfrgut.txt") as f:
            words = f.read().decode(encoding="iso-8859-1").split()

    word = random.choice(words)
    server_sock.sendto(word.encode(), MIDDLEWARE_ADDRESS)
    print("Mot aléatoire envoyé au middleware : {}".format(word))
