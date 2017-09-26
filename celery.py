from __future__ import absolute_import, unicode_literals
from celery import celery
from misc.constants import rabbitmq

app = Celery('proj',
                broker = rabbitmq,
                backend = rabbitmq,
                include = ['tasks'])

if __name__ == "__main__":
    app.start()
