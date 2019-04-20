import multiprocessing
import time
import os

# 进程：
# 	1、资源的集合，操作系统进行资源分配和调度的基本单位，多个进程之间相互独立
# 	2、稳定性好，如果一个进程崩溃，不影响其他进程，但是进程消耗资源大，开启的进程数量有限制

# 进程都是由父进程产生的

def run():
    # print("start....")
    print('parent proccess',os.getppid())
    print('my pid',os.getpid())
    time.sleep(2)

if __name__ == '__main__':
    run()
    p = multiprocessing.Process(target=run)
    p.start()
    # p1 = multiprocessing.Process(target=run)
    # p1.start()
    # print(multiprocessing.current_process())
