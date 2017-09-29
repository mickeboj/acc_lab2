# Code for Applied Cloud Computing Lab 2

### To test api
http://130.239.81.131:5000/wordcount/api/v1.0/get_wordcount


## Packages installed on VM

### Python
sudo apt-get update
sudo apt-get install -y python python-pip
sudo -H pip install --upgrade pip
pip install celery


### rabbitmq
sudo apt-get install rabbitmq server

### starting and stopping
sudo rabbitmq-server

sudo rabbitmq-server -detached

$ sudo rabbitmqctl stop


## Setting up

### celery with rabbit mq running
In .py file:

from celery import Celery

app = Celery('tasks', broker='amqp://<user>:<pwd>@localhost:5672/<hostname>')

@app.task
def add(x, y):
    return x + y


For running worker:

celery -A tasks worker --loglevel=info


### rabbitmq
sudo rabbitmqctl add_user <user> <pwd>
sudo rabbitmqctl add_vhost <hostname>
sudo rabbitmqctl set_user_tags <user> <tag>
sudo rabbitmqctl set_permissions -p <hostname> <user> ".*" ".*" ".*"
