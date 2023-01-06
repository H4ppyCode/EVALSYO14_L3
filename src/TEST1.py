import socket
import random

# Génère un mot aléatoire de 5 lettres
def générer_mot():
    lettres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    mot = ''
    for i in range(5):
        mot += random.choice(lettres)
    return mot

# Crée un socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Lie le socket à une adresse IP et un port
server_socket.bind(('', 1234))

# Écoute les connexions entrantes
server_socket.listen()

while True:
    # Accepte une connexion
    client_socket, client_address = server_socket.accept()

    # Génère un mot aléatoire pour cette session de jeu
    mot_à_deviner = générer_mot()

    while True:
        # Reçoit une devinette du client
        devinette = client_socket.recv(1024).decode()

        # Vérifie si la devinette est correcte
        indices_corrects = 0
        for i in range(len(devinette)):
            if devinette[i] == mot_à_deviner[i]:
                indices_corrects += 1

        # Envoie un message au client indiquant le nombre d'indices corrects
        client_socket.send(f"{indices_corrects} indices corrects".encode())

        # Si tous les indices sont corrects, le jeu est terminé
        if indices_corrects == 5:
            break

# Ferme la connexion avec le client
client_socket.close()
