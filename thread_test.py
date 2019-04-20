import threading
import time


def run(n, m):
    print("task ", n)
    print(threading.current_thread())
    time.sleep(m)
    print("%s sleep over." % n)


t1 = threading.Thread(target=run, args=("t1", 4))
t2 = threading.Thread(target=run, args=("t2", 4))
t3 = threading.Thread(target=run, args=("t3", 2))

t1.setDaemon(True)
t1.start()
t2.setDaemon(True)
t2.start()
t3.start()

print(threading.main_thread())
print(threading.active_count())
print('main thread over.')

# run("t1")
# run("t2")
