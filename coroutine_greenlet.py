# 协程：用户自己控制的，微线程，不由CPU调度，协程能保留上一次调用时的状态，遇到IO操作就切换。
# 单线程下实现并发的效果。
# 无需线程切换的消耗
# 无需锁及同步开发
# 高并发，高扩展，低成本

# 缺点
# 无法运用多核的资源
# 协程需要和进程配合才能运行在多CPU上

import time, queue
from greenlet import greenlet as gt

def fun1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()


def fun2():
    print(56)
    gr1.switch()
    print(78)

# if __name__ == '__main__':
gr1 = gt(fun1)
gr2 = gt(fun2)
gr1.switch()
