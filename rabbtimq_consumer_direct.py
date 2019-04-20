import pika


def backcall(ch, method, properties, body):
    print(ch, method, properties, body)
    print(body)
    # auto_ack=false时，需要进行手动确认
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print('我处理完了！')


# 建立socket
consumer = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# 声明管道
channel = consumer.channel()
#
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')
# 不指定queue名称，exclusive=True随机生成queue，会在queue消息使用后，自动删除queue
queue = channel.queue_declare(queue='', exclusive=True)
queue_name = queue.method.queue
severities = ['info','warning','error']
for severity in severities:
    channel.queue_bind(
        exchange='direct_logs',
        queue=queue_name,
        routing_key=severity
    )

channel.basic_consume(on_message_callback=backcall,  # 收到消息后的处理函数
                      queue=queue_name,
                      auto_ack=False)
channel.start_consuming()
