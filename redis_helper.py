import redis


class RedisHelper():
    def __init__(self):
        self.conn = redis.Redis(host='127.0.0.1', port=6379, db=0)
        #发布消息的频道
        self.channel_pub = 'fm101.5'
        #接收消息的频道
        self.channel_sub = 'fm101.5'

    def publish(self, msg):
        self.conn.publish(self.channel_pub, msg)
        return True

    def subscribe(self):
        # 开始订阅，打开收音机
        pub = self.conn.pubsub()
        # 调频道
        pub.subscribe(self.channel_sub)
        # 准备接收
        pub.parse_response()
        return pub


# obj = RedisHelper()
# redis_sub = obj.subscribe()
#
# while True:
#     msg = redis_sub.parse_response()
#     print(msg)

conn = redis.Redis(host='127.0.0.1', port=6379, db=0)
pub = conn.pubsub()
# 调频道
pub.subscribe('fm101.5')
while True:
    # 准备接收
    print(pub.parse_response())



