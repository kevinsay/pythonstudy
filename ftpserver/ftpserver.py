# First, you must create a request handler处理类 class by subclassing the BaseRequestHandler class and overriding覆盖 its handle() method; this method will process incoming requests. 　　
# 你必须自己创建一个请求处理类，并且这个类要继承BaseRequestHandler,并且还有重写父亲类里的handle()
# Second, you must instantiate实例化 one of the server classes, passing it the server’s address and the request handler class.
# 你必须实例化TCPServer ，并且传递server ip 和 你上面创建的请求处理类 给这个TCPServer
# Then call the handle_request() or serve_forever() method of the server object to process one or many requests.
# server.handle_request() #只处理一个请求
# server.serve_forever() #处理多个一个请求，永远执行
import socketserver
import json
import os


# class MyTcpHander(socketserver.BaseRequestHandler):
#     def __init__(self, request, client_address, server):
#         socketserver.BaseRequestHandler.__init__(self, request, client_address, server)
#         self.client_address = client_address
#
#     def handle(self):
#         while True:
#             try:
#                 data = self.request.recv(1024).strip()
#                 if not data:
#                     print(self.client_address+'断开了.')
#                     break
#                 self.request.sendall(data)
#             except ConnectionResetError as msg:
#                 print('except',msg)
#                 break

class FTPServer(socketserver.BaseRequestHandler):
    def __init__(self, request, client_address, server):
        socketserver.BaseRequestHandler.__init__(self, request, client_address, server)
        self.client_address = client_address

    def handle(self):
        while True:
            try:
                data = self.request.recv(1024).strip()
                print(data)
                if not data:
                    print(self.client_address + '断开了.')
                    break
                cmd_dict = json.loads(data.decode())
                print('cmd_dict', cmd_dict)
                action = cmd_dict['action']
                if hasattr(self, action):
                    func = getattr(self, action)
                    func(cmd_dict)
            except ConnectionResetError as msg:
                print('except', msg)
                break

    def upload(self, *args):
        cmd_dic = args[0]
        filename = cmd_dic["filename"]
        filesize = cmd_dic["filesize"]
        print('filesize', filesize)
        print('filename', filename)
        with open(filename, "wb") as f:
            self.request.send(b'ok,begin upload data.')
            received_size = 0
            while received_size < filesize:
                data = self.request.recv(1024)
                f.write(data)
                received_size += len(data)
            else:
                print('%s has upload.' % filename)



if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 6969), FTPServer)
    server.serve_forever()
    pass
