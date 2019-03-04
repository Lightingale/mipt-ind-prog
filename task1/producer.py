#!/usr/bin/env python
import random
import time
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

while True:
    sleep_interval = random.randint(0, 13)
    rand_num = random.randint(0, 1337)

    channel.basic_publish(exchange='',
                            routing_key='queue',
                            body=str(rand_num))
    time.sleep(sleep_interval)
connection.close()
        
