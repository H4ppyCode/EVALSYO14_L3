class NameServer:
    def __init__(self):
        self.game_servers = {}

    def register_game_server(self, name, ip_address):
        self.game_servers[name] = ip_address

    def get_random_game_server(self):
        name = random.choice(list(self.game_servers.keys()))
        ip_address = self.game_servers[name]
        return (name, ip_address)


server = NameServer()
server.register_game_server("Server 1", "192.168.1.1")
server.register_game_server("Server 2", "192.168.1.2")
server.register_game_server("Server 3", "192.168.1.3")

name, ip_address = server.get_random_game_server()
print(name, ip_address)
