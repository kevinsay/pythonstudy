import pika


def backcall(ch, method, properties, body):
    print(ch, method, properties, body)
    print(body)
    # auto_ack=false时，需要进行手动确认
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print('我处理完了！')


# 建立socket连接
consumer = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# 声明管道
channel = consumer.channel()
#
channel.exchange_declare(exchange='logs', exchange_type='fanout')
# 不指定queue名称，exclusive=True随机生成queue，会在queue消息使用后，自动删除queue
queue = channel.queue_declare(queue='', exclusive=True)
queue_name = queue.method.queue
print(queue_name)
# 绑定到exchange转发器
channel.queue_bind(exchange='logs', queue=queue_name)

channel.basic_consume(on_message_callback=backcall,  # 收到消息后的处理函数
                      queue=queue_name,
                      auto_ack=False)
channel.start_consuming()
