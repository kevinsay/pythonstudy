import redis
import time

# r = redis.Redis(host='127.0.0.1',port=6379)
# print(r.get('name'))

pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0)
print(pool)
r = redis.Redis(connection_pool=pool)
print(r.keys())
# exit()

# print(r.get('name').decode())
# r.set('mylist',[1,2,3,4])
# print(r.get('mylist').decode())

print(r.hgetall('user_info_3'))
print(r.hget('user_info_3','username'))
exit()

pipe = r.pipeline(transaction=False)
pipe.set('age', 22)
# time.sleep(50)
pipe.set('role', 'sb')
# pipe.set()

pipe.execute()

