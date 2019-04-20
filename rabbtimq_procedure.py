import pika

# 生产者

# 创建socket连接
procedure = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# 声明一个管道
channel = procedure.channel()
# 管道中声明一个队列,durable=True进行队列持久化，
# channel.queue_declare(queue='hello2')
#队列进行持久化，发消息时进行持久化，服务重启后，消息保存
channel.queue_declare(queue='hello4', durable=True)
#队列不进行持久化，发消息时进行持久化，服务重启后，消息丢失
# channel.queue_declare(queue='hello5')
channel.basic_publish(
    exchange='', routing_key='hello4', body='Hello1',
    properties=pika.BasicProperties(
        delivery_mode=2,  # 消息持久化
    )
)
procedure.close()
