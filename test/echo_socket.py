import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost', 50000))
s.listen(1)
conn, addr = s.accept()

print(f"новый сокет для общения с клиентом -{conn}")
print(f"addr: адрес клиента (IP-адрес и порт) - {addr}")

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.sendall(data)
conn.close()
