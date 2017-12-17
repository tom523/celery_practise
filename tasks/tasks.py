from celery import Celery
import time

app = Celery('proj', backend='rpc://', broker='pyamqp://guest@localhost//')


@app.task
def add(x, y):
    time.sleep(6)
    return x + y
