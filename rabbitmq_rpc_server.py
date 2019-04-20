import pika


def onrequest(ch, method, props, body):
    response = body
    ch.basic_publish(
        exchange='',
        routing_key=props.reply_to,
        properties=pika.BasicProperties(correlation_id=props.correlation_id),
        body=response
    )
    # 任务完成，给客户端确认
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print('我处理完了！')


# 建立socket连接
service = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# 声明管道
channel = service.channel()
#
channel.queue_declare(queue='rpc_queue')

channel.basic_consume(on_message_callback=onrequest,  # 收到消息后的处理函数
                      queue='rpc_queue',
                      auto_ack=False)
channel.start_consuming()
