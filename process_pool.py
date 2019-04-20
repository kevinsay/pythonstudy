from multiprocessing import Pool, Process
import time
import os


# 进程池：同一时间CPU上运行多少个进程
def foo(i):
    print('进程%s开始执行' % os.getpid())
    time.sleep(2)


def callbackfun(i):
    # pass
    print("进程%s执行完毕" % os.getpid())


if __name__ == '__main__':
    pool = Pool(5)
    for i in range(10):
        # 同步
        # pool.apply(func=foo, args=(i,))
        # 异步,回调函数是在父进程中执行的
        pool.apply_async(func=foo, args=(i,), callback=callbackfun)

    pool.close()
    # pool.join()  # 等待所有进程结束，不join的话就直接退出
    pool.join()
