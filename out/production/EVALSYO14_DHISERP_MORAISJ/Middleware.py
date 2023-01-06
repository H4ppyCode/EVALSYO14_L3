import socket

# Adresse et port du serveur
SERVER_ADDRESS = ("localhost", 5000)

CLIENT_ADDRESS = ("localhost", 5002)

# Créez un socket en mode UDP
try:
    middleware_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Liez le socket à l'adresse et au port du middleware
    middleware_sock.bind(("localhost", 5001))

while True:
    middleware_sock.listen()
    conn, addr = middleware_sock.accept()

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
    # data2 = "ok"
    # print("Données envoyé au Client {} : {}".format(addr, data2))
    # middleware_sock.sendto(data2.encode(), CLIENT_ADDRESS)
    word = "yess"
    middleware_sock.sendto(word.encode(), CLIENT_ADDRESS)
    print("Mot  envoyé au client : {}".format(word))
