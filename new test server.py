import socket
import threading

class BattleshipsServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []
        self.ships_data = {}
        self.setup_server()

    def setup_server(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server listening on {self.host}:{self.port}")
        threading.Thread(target=self.accept_clients).start()

    def accept_clients(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Connection from {client_address}")
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        player_name = client_socket.recv(1024).decode()
        print(f"{player_name} joined the game.")
        self.clients.append(client_socket)

        if len(self.clients) == 2:
            self.notify_players("welcome2")

        while True:
            try:
                data = client_socket.recv(1024).decode()
                if not data:
                    break
                if data.startswith("Ships"):
                    self.ships_data[player_name] = eval(data.split(" ", 1)[1])
                    if len(self.ships_data) == 2:
                        self.notify_players("Ships " + str(self.ships_data))
                        print("Game started.")
                elif data.startswith("Shot"):
                    opponent_socket = self.get_opponent_socket(client_socket)
                    opponent_socket.send(data.encode())
            except Exception as e:
                print(f"Error handling client {player_name}: {e}")
                break

        print(f"{player_name} disconnected.")
        self.clients.remove(client_socket)
        client_socket.close()

    def notify_players(self, message):
        for client in self.clients:
            client.send(message.encode())

    def get_opponent_socket(self, current_socket):
        return next(client for client in self.clients if client != current_socket)

def main():
    host = "10.112.193.195"
    port = 8080
    server = BattleshipsServer(host, port)

if __name__ == "__main__":
    main()