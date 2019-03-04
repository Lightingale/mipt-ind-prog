#!/usr/bin/env python
import time
import sys, traceback
import pika

parameters = pika.ConnectionParameters('rabbit', 5672)

while True:
    try:
        connection = pika.BlockingConnection(parameters)
        break
    except pika.exceptions.AMQPConnectionError:
        print('Cannot connect yet, retrying')
        time.sleep(3)
    except (pika.exceptions.ConnectionClosed, OSError):
        print('Connection closed, retrying')
        time.sleep(3)
channel = connection.channel()
print('Connected successfully')

channel.queue_declare(queue='queue')

print("Waiting for messages. To exit press CTRL+C")

def callback(ch, method, properties, body):
    print(body.decode())
    channel.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(callback, queue='queue')

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
except Exception:
    channel.stop_consuming()
    traceback.print_exc(file=sys.stdout)
