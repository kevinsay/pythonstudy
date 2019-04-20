import pika
import uuid
import time


class RpcClient:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        # 随机生成唯一queue,使用后自动销毁
        queue = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = queue.method.queue
        self.channel.basic_consume(
            on_message_callback=self.on_response,
            auto_ack=False,
            queue=self.callback_queue
        )

    # 收到消息的回调函数
    def on_response(self, ch, method, properties, body):
        if self.corr_id == properties.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_queue',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,#服务器执行完返回消息的queue
                correlation_id=self.corr_id
            ),
            body=str(n)
        )
        while self.response is None:
            print('no msg..')
            # 非阻塞模式的start_consuming
            self.connection.process_data_events()
            time.sleep(0.5)

        return int(self.response)


rpc_client = RpcClient()
print(rpc_client.call(10))
