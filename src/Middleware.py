import socket

# Adresse et port du serveur
SERVER_ADDRESS = ("localhost", 5000)

CLIENT_ADDRESS = ("localhost", 5002)

# Créez un socket en mode UDP
middleware_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Liez le socket à l'adresse et au port du middleware
middleware_sock.bind(("localhost", 5001))

while True:
    # Recevez des données envoyées par le client
    data, addr = middleware_sock.recvfrom(1024)
    data = data.decode()
    print("Données reçues du client {} : {}".format(addr, data))

    # Envoyez les données au serveur
    middleware_sock.sendto(data.encode(), SERVER_ADDRESS)

    # Recevez une réponse du serveur
    data, addr = middleware_sock.recvfrom(1024)
    data = data.decode()
    print("Données reçues du serveur {} : {}".format(addr, data))
    # Recevez une réponse du serveur
    data, addr = middleware_sock.recvfrom(1024)

    data = data.decode()
    print("Données reçues du serveur {} : {}".format(addr, data))
    # Envoyez la réponse au client
    middleware_sock.sendto(data.encode(), addr)

    # Envoyer ok au client
    data = "ok"
    print("Données envoyé au Client {} : {}".format(addr, data))
    middleware_sock.sendto(data.encode(), SERVER_ADDRESS)


    data, addr = "check moi ça"
    data = data.decode()
    middleware_sock.sendto(data.encode(), SERVER_ADDRESS)
    print('okay')