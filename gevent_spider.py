from urllib import request
import gevent
import time

# gevent默认是检测不到urllib的IO操作
# 给当前程序中的有可能进行IO操作的地方打标，便于gevent进行IO切换。

from gevent import monkey
monkey.patch_all()

def f(url):
    resp = request.urlopen(url)
    data = resp.read()
    f = open('url.html', "wb")
    f.write(data)
    f.close()
    print("received %s data from %s" % (len(data), url))

begin = time.time()
# f("https://www.cnblogs.com/alex3714/category/770733.html")
# f("https://www.cnblogs.com/alex3714/category/770733.html")
# f("https://www.cnblogs.com/alex3714/category/770733.html")
# end = time.time()
# print('used time', end - begin)

gevent.joinall([gevent.spawn(f, "https://www.cnblogs.com/alex3714/category/770733.html"),
                gevent.spawn(f, "https://www.cnblogs.com/alex3714/category/770733.html"),
                gevent.spawn(f, "https://www.cnblogs.com/alex3714/category/770733.html")])

end = time.time()
print('used time', end - begin)
