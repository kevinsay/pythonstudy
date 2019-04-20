# 队列

# 列表和队列的区别

# 从列表中取出来的数据，数据还在列中
# 队列中数据只有一份，取走就没有了
import queue

# # 先入先出
# # 默认大小没有限制
# q = queue.Queue()#先入先出队列 FIFO
# q.put("d1")
# print(q.qsize())
# print(q.full())
# #put添加队列元素，默认block=True，队列填满后，就会等待卡住，可设置block=False
# q.put("d2",block=False)
# q.put("d3")
# #get方法获取队列元素，默认block=true,取完队列元素后，就会等待,可设置block=False,或者使用q.get_nowait()
# while True:
#     print(q.get(block=False))

# q = queue.LifoQueue()  # 后入先出队列:LIFO
# q.put(1)
# q.put(2)
# print(q.get())

# q = queue.PriorityQueue()  # 可设置优先级队列
# q.put((1, "abc"))
# q.put((10, "def"))
# q.put((11, "ddz"))
# q.put((8, "syt"))
#
# while True:
#    print(q.get())

import threading
import time

q = queue.Queue()


def procedure():
    i = 1
    while True:
        q.put(i)
        print("添加骨头%s" % i)
        # time.sleep()
        i += 1

def consumer(name):
    while True:
        print("%s取到了骨头%s" % (name, q.get()))


p = threading.Thread(target=procedure)
p.start()
c1 = threading.Thread(target=consumer, args=('dahuang',))
c1.start()
c2 = threading.Thread(target=consumer, args=('gaofei',))
c2.start()

