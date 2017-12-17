# -*- coding:utf-8 -*-
from celery import Celery
from time import sleep

'''
第一个参数会添加到任务上用来区分它们。backend参数是可选的，
如果想要查询任务状态或者任务执行结果时必填。broker参数表示
用来连接broker的URL，rabbitmq采用的是一种称为’amqp’的协
议，如果rabbitmq运行在默认设置下，celery不需要其他信息，只
要amqp://即可。
'''

# app = Celery('tasks', backend='amqp', broker='amqp://')
app = Celery('tasks')
app.config_from_object('celeryconfig')


# 这个hello函数不需要返回有用信息，设置ignore_rsult可以忽略任务结果
@app.task(ignore_result=True)
def hello():
    print 'Hello,Celery!'


@app.task
def add(x, y):
    sleep(5)
    return x + y