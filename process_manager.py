from multiprocessing import Manager, Process
import os


def f(d, l):
    d[os.getpid()] = os.getppid()
    l.append(os.getpid())
    print(d, l)


if __name__ == '__main__':
    # 进程之间数据共享
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(5))
        p_list = []
        for i in range(10):
            p = Process(target=f, args=(d, l))
            p_list.append(p)
            p.start()

        for p in p_list:
            p.join()

        print(d)
        print(l)
