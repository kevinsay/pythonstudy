import threading
import time


def run(n):
    #获取锁
    lock.acquire()
    print('thread ', n)
    global num
    num += 1
    #释放锁
    lock.release()
    # time.sleep(2)

lock = threading.Lock()
num = 0
thread_list = []
for i in range(51):
    thread = threading.Thread(target=run, args=(i,))
    thread.start()
    thread_list.append(thread)

for thread in thread_list:
    thread.join()
# time.sleep(3)

print('num', num)
