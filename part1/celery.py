from celery import celery
from ../misc/constants import rabbitmq

app = Celery('proj',
                broker = rabbitmq,
                backend = rabbitmq,
                include = ['part1.count.wordcount'])

if __name__ == "__main__":
    app.start()
