import multiprocessing

# 进程的内存是独立的,进程间要进行交流可以使用以下方式
from multiprocessing import Queue, Pipe


def run():
    q.put([42, 11])


def run1(q):
    q.put([42, 11])


def run2(conn):
    conn.send([1,1,2])
    print(conn.recv())
    conn.close()


if __name__ == '__main__':
    # q = Queue()
    # p1= multiprocessing.Process(target=run)
    # p1.start()
    # p2 = multiprocessing.Process(target=run1, args=(q,))
    # p2.start()
    # print(q.get())

    parent_conn, child_conn = Pipe()
    p = multiprocessing.Process(target=run2, args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    parent_conn.send("hello")