from multiprocessing import Process, Lock


def run(i, l):
    l.acquire()
    print('进程%s' % i)
    l.release()


if __name__ == '__main__':
    lock = Lock()
    for i in range(10):
        p = Process(target=run, args=(i, lock))
        p.start()
