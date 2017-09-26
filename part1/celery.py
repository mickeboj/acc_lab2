from celery import celery
from ../misc/constants import rabbitmq

app = Celery('p1cell',
                broker = rabbitmq,
                backend = rabbitmq,
                include = ['part1.count.wordcount'])
