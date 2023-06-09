import pika
import json

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

channel.queue_declare(queue='auth')


def publish(body):
    channel.basic_publish(exchange='', routing_key='auth', body=json.dumps(body))