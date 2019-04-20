import pika

# 建立socket连接
procedure = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# 声明管道
channel = procedure.channel()
# 声明广播
channel.exchange_declare(exchange='topic_logs', exchange_type='topic')
# 级别
severity = 'mysql.info'
# 准备发送广播
channel.basic_publish(
    exchange='topic_logs',
    routing_key=severity,
    body='这是一个mysql info'
)
print('消息已发送。')
procedure.close()
