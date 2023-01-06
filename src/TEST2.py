import socket

# Crée un socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Se connecte au serveur
client_socket.connect(('localhost', 1234))

while True:
    # Affiche un message pour inviter le joueur à saisir une devinette
    devinette = input("Entrez une devinette de 5 lettres: ")

    # Envoie la devinette au serveur
    client_socket.send(devinette.encode())

    # Reçoit un message du serveur indiquant le nombre d'indices corrects
    indices_corrects = client_socket.recv(1024).decode()
    print(indices_corrects)

    # Si tous les indices sont corrects, le jeu est terminé
    if "5 indices corrects" in indices_corrects:
        break

# Ferme la connexion avec le serveur
client_socket.close()
