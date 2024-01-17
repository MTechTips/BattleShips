import tkinter as tk
import socket
import threading

class BattleshipsGame:
    def __init__(self, root, player_name, server_address, server_port):
        self.root = root
        self.root.title("Battleships Game")

        self.player_name = player_name
        self.server_address = server_address
        self.server_port = server_port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect_to_server()

        self.board_size = 5
        self.board = [['O' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.ships = []
        self.ship_coordinates = []

        self.create_board_buttons()

        # Start a thread to listen for messages from the server
        threading.Thread(target=self.receive_messages).start()

    def connect_to_server(self):
        try:
            self.client_socket.connect((self.server_address, self.server_port))
            self.client_socket.send(self.player_name.encode())
        except Exception as e:
            print(f"Error connecting to server: {e}")

    def create_board_buttons(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                button = tk.Button(self.root, text=' ', width=3, height=2,
                                   command=lambda i=i, j=j: self.handle_click(i, j))
                button.grid(row=i, column=j)

    def handle_click(self, row, col):
        if len(self.ships) < 7:
            self.place_ship(row, col)
        else:
            self.client_socket.send(f"Shot {row} {col}".encode())

    def place_ship(self, row, col):
        if (row, col) not in self.ship_coordinates:
            self.ship_coordinates.append((row, col))
            self.board[row][col] = 'S'
            if len(self.ship_coordinates) == 4:
                self.ships.append(self.ship_coordinates.copy())
                self.ship_coordinates = []
                print(f"Ship {len(self.ships)} placed.")
                if len(self.ships) == 7:
                    self.client_socket.send(f"Ships {self.ships}".encode())
            self.update_board()

    def receive_messages(self):
        while True:
            try:
                data = self.client_socket.recv(1024).decode()
                if not data:
                    break
                self.process_message(data)
            except Exception as e:
                print(f"Error receiving messages: {e}")
                break

    def process_message(self, message):
        if message.startswith("Ships"):
            _, ships_str = message.split(" ", 1)
            ships = eval(ships_str)
            for ship in ships:
                for coord in ship:
                    self.board[coord[0]][coord[1]] = 'S'
        elif message.startswith("Shot"):
            _, row, col = message.split()
            row, col = int(row), int(col)
            if self.board[row][col] == 'S':
                self.board[row][col] = 'X'
                print("Hit!")
            else:
                print("Miss.")
        self.update_board()

    def update_board(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                button_text = 'X' if self.board[i][j] == 'X' else ' '  # Display hits only
                self.root.children[f'!button{i}!{j}'].config(text=button_text)

def main():
    player_name = input("Enter your name: ")
    server_address = input("Enter server address: ")
    server_port = int(input("Enter server port: "))

    root = tk.Tk()
    game = BattleshipsGame(root, player_name, server_address, server_port)
    root.mainloop()

if __name__ == "__main__":
    main()
