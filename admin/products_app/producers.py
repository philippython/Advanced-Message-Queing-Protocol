import pika
import json

params = pika.URLParameters("amqps://tnbvyjde:bEp76fHf5eCs3vn49-MTGBGCooijagf7@sparrow.rmq.cloudamqp.com/tnbvyjde")
connection = pika.BlockingConnection(parameters=params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange="", routing_key="main", body=json.dumps(body), properties=properties)
