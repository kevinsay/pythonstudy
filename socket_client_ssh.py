import socket
import hashlib

client = socket.socket()
client.connect(('127.0.0.1', 6969))

while True:
    text = input("请输入:")
    if len(text) == 0:
        continue
    client.send(text.encode('utf-8'))
    # res_data_len = client.recv(1024)
    # client.send("准备好接收".encode('utf-8'))
    # print('res_data_len:',res_data_len)
    # rece_size = 0
    # rece_data = b''
    # while rece_size < int(res_data_len.decode('utf-8')):
    #     data = client.recv(1024)
    #     rece_size += len(data)
    #     rece_data += data
    # else:
    #     print("receive done.")
    #     print(rece_data.decode("utf-8"))
    m = hashlib.md5()
    total_file_size = client.recv(1024)
    total_file_size = int(total_file_size.decode('utf-8'))
    print('total_file_size:', total_file_size)
    client.send('准备好接收文件!'.encode('utf-8'))
    received_size = 0
    with open("receive.txt", "wb") as rf:
        while received_size < total_file_size:
            size = total_file_size - received_size
            if size >= 1024:
                size = 1024
            linedata = client.recv(size)
            received_size += len(linedata)
            rf.write(linedata)
            m.update(linedata)
        else:
            print('receive done.')

        print('client_received_md5', m.hexdigest())
        server_received_md5 = client.recv(1024)
        print('server_received_md5', server_received_md5)

client.close()
