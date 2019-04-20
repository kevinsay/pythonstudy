import pika

# 建立socket连接
procedure = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# 声明管道
channel = procedure.channel()
# 声明广播
channel.exchange_declare(exchange='logs', exchange_type='fanout')
# 准备发送广播
channel.basic_publish(exchange='logs', routing_key='', body='这是一个广播，不需要queue')
print('广播消息已发送。')
procedure.close()
