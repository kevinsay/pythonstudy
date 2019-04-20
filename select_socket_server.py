# SOCKET IO多路复用
import socket
import select
import queue

# conn_quene = queue.Queue()
msg_dict = {}
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 6969))
server.listen()
# 设置socket非阻塞
server.setblocking(False)
# 初始化监测socket链接，先监测自身
inputs = [server]
outputs = []
while True:
    readable, writeable, exceptional = select.select(inputs, outputs, inputs)
    # print(readable)
    # print(writeable)
    # print(exceptional)
    for r in readable:
        if r is server:  # 代表有新链接建立
            conn, addr = server.accept()
            print('来了一个新链接', conn, addr)
            inputs.append(conn)  # 加入到监测链接列表，现在想要server知道这个客户端发送数据过来，就需要select监测这个链接
            msg_dict[conn] = queue.Queue()  # 给该链接建立一个消息队列
        else:
            data = r.recv(1024)
            msg_dict[r].put(data)
            print(data)
            outputs.append(r)  # 记录需要给客户端返回消息的socket链接
            # r.send(data)

    # 等同于直接使用r.send(data)
    for w in writeable:  # 返回给客户端的socket链接
        data_to_clinet = msg_dict[w].get()
        w.send(data_to_clinet)
        # 确保下次循环的时候，writeable不返回已经处理完的链接
        outputs.remove(w)

    # 处理客户端链接的连接异常，删除该监听
    for e in exceptional:
        if e in outputs:
            outputs.remove(e)
        inputs.remove(e)
        del msg_dict[e]
