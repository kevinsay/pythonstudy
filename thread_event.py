import threading
import time

event = threading.Event()


# 等待标志位设定,Block until the internal flag is true.
# event.wait()
# Set the internal flag to true.
# event.set()
# Reset the internal flag to false.
# event.clear()

def lighter():
    count = 0
    event.set()
    while True:
        if count > 5 and count < 10:
            event.clear()
            print("红灯亮起")
        elif count > 10:
            event.set()
            count = 0
        else:
            print("绿灯亮起")
        count += 1
        time.sleep(1)


def car(name):
    while True:
        if event.is_set():
            print("car %s running..." % name)
        else:
            print("car %s waiting..." % name)
            event.wait()
            print("light change to green.")
        time.sleep(1)


light = threading.Thread(target=lighter)
light.start()

car1 = threading.Thread(target=car,args=('特斯拉',))
car1.start()
car2 = threading.Thread(target=car,args=('奔驰',))
car2.start()


