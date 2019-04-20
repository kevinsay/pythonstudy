import pika
import time

def backcall(ch, method, properties, body):
    print(ch, method, properties, body)
    time.sleep(30)
    print(body)
    #auto_ack=false时，需要进行手动确认
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print('我处理完了！')


# 消费者

# 建立socket连接
consumer = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# 建立管道
channel = consumer.channel()
# 管道中声明一个队列,除非你确认生产者中已经声明这个队列，并且已经启动
channel.queue_declare(queue='hello4',durable=True)
# 准备收消息
channel.basic_qos(prefetch_count=2)
channel.basic_consume(on_message_callback=backcall,  # 收到消息后的处理函数
                      queue='hello4',
                      auto_ack=False)
channel.start_consuming()