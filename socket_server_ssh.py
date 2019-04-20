import socket
import os
import hashlib

server = socket.socket()
server.bind(('127.0.0.1', 6969))
# 监听
server.listen()
# 接听
conn, addr = server.accept()
while True:
    # print(conn,addr)
    while True:
        data = conn.recv(200)
        if not data:
            print("客户端已断开")
            break
        print("你发给我的信息是:%s" % data)
        # send_msg = os.popen(data.decode()).read()
        # print(len(send_msg))
        # conn.send(str(len(send_msg.encode())).encode("utf-8"))
        # #等待客户端响应，避免粘包
        # client_ack = conn.recv(1024)
        # print(client_ack.decode('utf-8'))
        # conn.send(send_msg.encode('utf-8'))
        m = hashlib.md5()
        cmd, filename = data.decode().split()
        if os.path.isfile(filename):
            f = open(filename,'rb')
            file_size = os.stat(filename).st_size
            conn.send(str(file_size).encode())
            client_ack = conn.recv(1024)
            for line in f:
                conn.send(line)
                m.update(line)
            f.close()

        conn.send(m)


server.close()
