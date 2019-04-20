import gevent
from gevent import socket

def server(port):
    s = socket.socket()
    s.bind(("127.0.0.1", port))
    s.listen()
    while True:
        conn, addr = s.accept()
        gevent.spawn(hander_request, conn)


def hander_request(conn):
    while True:
        data = conn.recv(1024)
        print("recv data", data)
        conn.send(data)
        if not data:
            conn.shutdown(socket.SHUT_WR)


if __name__ == '__main__':
    server(6969)
