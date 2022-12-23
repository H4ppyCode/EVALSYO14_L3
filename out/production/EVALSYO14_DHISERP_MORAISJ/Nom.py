#Ecouter la connexion d'un serveur au middleware
# Le middleware enregistre l'adresse ip du joueur dans Nom.py
# Nom.py renvoie un nom au hasard

import socket
import random

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('127.0.0.1', 5000)
sock.bind(server_address)

# Generate a list of random names
names = ['Marduk', 'Bob', 'Jin', 'Dragunov', 'Bryan', 'Kazuya']

while True:
    # Wait for a connection
    print('waiting for a connection')
    data, address = sock.recvfrom(4096)

    print('received %s bytes from %s' % (len(data), address))
    print('data: %s' % data)

    if data:
        # Choose a random name from the list
        name = random.choice(names)
        print('sending name "%s" back to the client' % name)
        sock.sendto(name.encode(), address)