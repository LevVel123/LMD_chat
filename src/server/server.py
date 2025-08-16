import socket
import threading
import argparse

class ChatServer:
    def __init__(self, host='0.0.0.0', port='5555'):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()
        self.clients = []
        self.nicknames = []

    def broadcast(self, message):
        for client in self.clients:
            client.send(message)
    
    def hanfle(self, client):
        while True:
            try:
                message = client.recv(1024)
                self.broadcast(message)
            except:
                index = self.clients.index(client)
                self.clients.remove(client)
                client.close()
                nickname = self.nicknames[index]
                self.broadcast(f'{nickname} has left the chat'.encode('utf-8'))
                self.nicknames.remove(nickname)
                break

    def receive(self):
        print("Server is running...")
        while True:
            client, address = self.server.accept()
            print(f"Connected with {str(address)}")

            client.send('NICK'.encode('utf-8'))
            nickname = client.recv(1024).decode('utf-8')
            self.nicknames.append(nickname)
            self.clients.append(client)

            print(f"Nickname-client: {nickname}")
            self.broadcast(f'{nickname} has joined the chat'.encode('utf-8'))
            client.send("Connected".encode('utf-8'))

            thread = threading.Thread(target=self.hanfle, args=(client,))
            thread.start()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Chat Server start')
    parser.add_argument('--host', default='0.0.0.0', help='IP adress of server')
    parser.add_argument('--port', type=int, default=5555, help='Port of server')
    args = parser.parse_args()

    server = ChatServer(args.host, args.port)
    server.receive()