import socket

server = socket.socket()
server.bind(('127.0.0.1', 6969))
# 监听
server.listen()
# 接听
conn, addr = server.accept()
while True:
    # print(conn,addr)
    data = conn.recv(1024)
    print("你发给我的信息是:%s" % data)
    conn.send(data.upper())

server.close()
