import socket
import threading
import argparse
import sys

class ChatClient:
    def __init__(self, host='127.0.0.1', port=5555):
        self.host = host
        self.port = port
        self.nickname = input("Enter your nickname: ")
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))

    def receive(self):
        while True:
            try:
                message = self.client.recv(1024).decode('utf-8')
                if message == 'NICK':
                    self.client.send(self.nickname.encode('utf-8'))
                else:
                    print(message)
            except:
                print("Connection error!")
                self.client.close()
                break

    def write(self):
        while True:
            message = input('')
            if message.lower() == '\exit':
                self.client.close()
                sys.exit(0)
            self.client.send(f'{self.nickname}: {message}'.encode('utf-8'))

    def run(self):
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

        write_thread = threading.Thread(target=self.write)
        write_thread.start()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Connecting to the chat-server')
    parser.add_argument('--host', default='127.0.0.1', help='Server IP address')
    parser.add_argument('--port', type=int, default=5555, help='Server port')
    args = parser.parse_args()

    client = ChatClient(args.host, args.port)
    client.run()