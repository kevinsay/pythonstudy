import threading
import time


def run(n):
    # 获取锁
    semaphore.acquire()
    # print('thread ', n)
    time.sleep(1)
    # global num
    # num += 1
    # 释放锁
    print("run the thread:%s\n" % n)
    semaphore.release()


# 互质锁：同一时刻允许一个线程修改数据
# 信号量：同一时刻允许一定数量的线程修改数据
semaphore = threading.BoundedSemaphore(5)
num = 0
thread_list = []
for i in range(22):
    thread = threading.Thread(target=run, args=(i,))
    thread.start()
    thread_list.append(thread)

while threading.active_count() != 1:
    print(threading.active_count())
else:
    print('all thread run done.')
# print('num', num)
