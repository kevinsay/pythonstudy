# 协程：用户自己控制的，微线程，不由CPU调度，协程能保留上一次调用时的状态，遇到IO操作就切换。
# 单线程下实现并发的效果。
# 无需线程切换的消耗
# 无需锁及同步开发
# 高并发，高扩展，低成本

# 缺点
# 无法运用多核的资源
# 协程需要和进程配合才能运行在多CPU上

import time, queue


def consumer(name):
    while True:
        new_baozi = yield
        print("%s is eating baozi %s" % (name, new_baozi))


def procedure():
    r = c1.__next__()
    r = c2.__next__()
    n = 0
    while n < 5:
        n += 1
        #唤醒生成器并传值
        c1.send(n)
        c2.send(n)
        print("procedure %s is making baozi."% n)


if __name__ == '__main__':
    c1 = consumer("c1")
    c2 = consumer("c2")
    procedure()
