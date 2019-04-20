import os
import json
import socket


class FTPClient():
    def __init__(self):
        self.client = socket.socket()

    def help(self):
        msg = '''
        ls
        pwd
        upload filename
        download filename
        '''
        print(msg)

    def connect(self, ip, port):
        self.client.connect((ip, port))

    def interactive(self):
        while True:
            cmd = input(">>").strip()
            if len(cmd) == 0: continue
            cmd_str = cmd.split()[0]
            if hasattr(self, cmd_str):
                func = getattr(self, cmd_str)
                func(cmd)
            else:
                self.help()

    def upload(self, *args):
        cmd_split = args[0].split(' ')
        if len(cmd_split) > 1:
            filename = cmd_split[1]
            if os.path.exists(filename):
                filesize = os.stat(filename).st_size
                file_dict = {
                    'action': 'upload',
                    'filename': filename,
                    'filesize': filesize,
                    "overriden": True
                }
                self.client.send(json.dumps(file_dict).encode())
                # 防止粘包，等待服务器确认
                server_response = self.client.recv(1024)
                with open(filename, "rb") as f:
                    for line in f:
                        self.client.send(line)
            else:
                print('%s is exist' % filename)

    def download(self):
        pass


if __name__ == '__main__':
    ftpclient = FTPClient()
    ftpclient.connect('127.0.0.1', 6969)
    ftpclient.interactive()
