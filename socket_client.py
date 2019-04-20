import socket

client = socket.socket()
client.connect(('127.0.0.1',6969))

while True:
    text = input("请输入：")
    client.send(text.encode('utf-8'))
    data = client.recv(1024)
    print(data.decode('utf-8'))
client.close()