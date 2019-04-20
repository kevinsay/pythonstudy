import pika

# 建立socket连接
procedure = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# 声明管道
channel = procedure.channel()
# 声明广播
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')
# 级别
severity = 'error'
# severity = 'info warning error'
# 准备发送广播
channel.basic_publish(exchange='direct_logs', routing_key=severity, body='这是一个info')
print('消息已发送。')
procedure.close()
