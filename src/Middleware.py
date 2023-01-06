# import socket
#
# # Adresse et port du serveur
# SERVER_ADDRESS = ("localhost", 6001)
#
# CLIENT_ADDRESS = ("localhost", 6000)
# JEU_ADDRESS = ("localhost", 6004)
# # Créez un socket en mode UDP
#
# middleware_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
# # Liez le socket à l'adresse et au port du middleware
# middleware_sock.bind(("localhost", 6002))
#
# while True:
#     # Recevez des données envoyées par le client
#     try:
#         data, addr = middleware_sock.recvfrom(1024)
#         data = data.decode()
#         print("Données reçues du client {} : {}".format(addr, data))
#
#         # Envoyez les données au serveur
#         middleware_sock.sendto(data.encode(), SERVER_ADDRESS)
#
#         # Recevez une réponse du serveur
#         data, addr = middleware_sock.recvfrom(1024)
#         data = data.decode()
#         print("Données reçues du serveur {} : {}".format(addr, data))
#
#         # Envoyer ok au client
#         check = "Le jeu peut commencer"
#         print("Données envoyé au Client {} : {}".format(CLIENT_ADDRESS, check))
#         middleware_sock.sendto(check.encode(), CLIENT_ADDRESS)
#
#         # Envoyer ok au client
#         print("Données envoyé au Jeu {} : {}".format(JEU_ADDRESS, data))
#         middleware_sock.sendto(data.encode(), JEU_ADDRESS)
#
#         data, addr = middleware_sock.recvfrom(1024)
#         data = data.decode()
#         print("Données reçues du jeux {} : {}".format(addr, data))
#     except:
#         pass
#
import socket
import time

# Adresse et port du serveur
SERVER_ADDRESS = ("localhost", 6001)

CLIENT_ADDRESS = ("localhost", 6000)
JEU_ADDRESS = ("localhost", 6004)
# Créez un socket en mode UDP

middleware_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Liez le socket à l'adresse et au port du middleware
middleware_sock.bind(("localhost", 6002))

while True:
    # Recevez des données envoyées par le client
    try:


        data, addr = middleware_sock.recvfrom(1024)
        data = data.decode()
        print("Données reçues du client {} : {}".format(addr, data))
        if data == "start game":
            # Envoyez les données au serveur
            middleware_sock.sendto(data.encode(), SERVER_ADDRESS)

            # Recevez une réponse du serveur
            data, addr = middleware_sock.recvfrom(1024)
            data = data.decode()
            print("Données reçues du serveur {} : {}".format(addr, data))

            mot = 'Indice : première lettre du mot ' + data[0].upper()
            # Envoyer ok au client
            check = "Le jeu peut commencer"
            print("Données envoyé au Client {} : {}".format(CLIENT_ADDRESS, check))
            middleware_sock.sendto(check.encode(), CLIENT_ADDRESS)

            # Envoyer le mot au Jeu
            print("Données envoyé au Jeu {} : {}".format(JEU_ADDRESS, data))
            middleware_sock.sendto(data.encode(), JEU_ADDRESS)

            # Recevoir le nb de lettres du mot a partir du jeu
            data, addr = middleware_sock.recvfrom(1024)
            data = data.decode()
            print("Données reçues du jeux {} : {}".format(addr, data))

            # Envoyer le nb au client
            print("Données envoyé au Client {} : {}".format(CLIENT_ADDRESS, data))
            middleware_sock.sendto(data.encode(), CLIENT_ADDRESS)

            # Envoyer la premiere lette au client
            print("Données envoyé au Client {} : {}".format(CLIENT_ADDRESS, mot))
            middleware_sock.sendto(mot.encode(), CLIENT_ADDRESS)

            for i in range(6):
                # Recevez une réponse du client #rep 1
                data, addr = middleware_sock.recvfrom(1024)
                data = data.decode()
                print("Données reçues du Client {} : {}".format(addr, data))

                # Envoyer la variable saisie au Jeu
                print("Données envoyé au Jeu {} : {}".format(JEU_ADDRESS, data))
                middleware_sock.sendto(data.encode(), JEU_ADDRESS)

                #Recevoir les instructions du jeu
                data, addr = middleware_sock.recvfrom(1024)
                data = data.decode()
                print("Données reçues du Jeu {} : {}".format(addr, data))

                print("Données envoyé au Client {} : {}".format(CLIENT_ADDRESS, data))
                middleware_sock.sendto(data.encode(), CLIENT_ADDRESS)

    except:
        pass
