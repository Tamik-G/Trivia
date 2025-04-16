import socket
import threading

server = "127.0.0.1", 50000
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.bind(("", 0))
client_socket.connect(server)
def read_socket():
    while True:
        data = client_socket.recv(1024)
        print(data.decode("utf-8"))

thread = threading.Thread(target=read_socket)
thread.start()

while True:
    message = input()
    client_socket.send(message.encode("utf-8"))