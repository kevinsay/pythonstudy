# 协程：用户自己控制的，微线程，不由CPU调度，协程能保留上一次调用时的状态，遇到IO操作就切换。
# 单线程下实现并发的效果。
# 无需线程切换的消耗
# 无需锁及同步开发
# 高并发，高扩展，低成本

# 缺点
# 无法运用多核的资源
# 协程需要和进程配合才能运行在多CPU上

# gevent中用到的主要模式是gevent

import gevent


def foo():
    print('running in foo')
    gevent.sleep(2)
    print('running in foo again.')


def bar():
    print('running in bar')
    gevent.sleep(1)
    print('running in bar agin.')


def fun():
    print('running in fun')
    gevent.sleep(0)
    print('running in fun again.')


gevent.joinall([gevent.spawn(foo), gevent.spawn(bar), gevent.spawn(fun)])
