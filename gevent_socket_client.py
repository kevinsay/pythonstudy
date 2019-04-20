import socket

client = socket.socket()
client.connect(("127.0.0.1",6969))
while True:
    text = input(">>:")
    client.send(text.encode())
    data = client.recv(1024)
    print(data)