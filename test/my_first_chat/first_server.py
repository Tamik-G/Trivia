import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# noinspection PyTypeChecker
sock.bind(("127.0.0.1", 5566))
clients = []

print("Start Server")
while True:
    data, adress = sock.recvfrom(1024)
    print(f"Message from [{adress}]: {data.decode('utf-8')}")
    if adress not in clients:
        clients.append(adress)
    for client in clients:
        if client == adress:
            continue
        sock.sendto(data, client)