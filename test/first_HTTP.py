import socket

HOST = "www.example.com"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, 80))

sock.send(f"GET / HTTP/1.1\r\nHost:{HOST}\r\n\r\n".encode())
response = sock.recv(4096)

sock.close()
print(response.decode())