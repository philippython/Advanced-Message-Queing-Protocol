import pika

params = pika.URLParameters("amqps://tnbvyjde:bEp76fHf5eCs3vn49-MTGBGCooijagf7@sparrow.rmq.cloudamqp.com/tnbvyjde")

connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue="admin")

def callback(ch, method, properties, body):
    print("[x] received %r" %body)

channel.basic_consume(queue="admin", on_message_callback=callback, auto_ack=True )

print(" [*] waiting for the messages. To exit press Ctrl-C")

channel.start_consuming()

