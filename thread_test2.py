import threading


def run1():
    lock.acquire()
    pass
    global num
    num += 1
    lock.release()
    return num


def run2():
    lock.acquire()
    global num2
    num2 += 1
    lock.release()
    return num2


def run3():
    lock.acquire()
    res = run1()
    pass
    res2 = run2()
    lock.release()
    print(res, res2)


num, num2 = 0, 0

# lock = threading.Lock():锁中锁
# 递归锁
lock = threading.RLock()
for i in range(10):
    t = threading.Thread(target=run3)
    t.start()

while threading.active_count() != 1:
    print(threading.active_count())
else:
    print('all thread done.')
