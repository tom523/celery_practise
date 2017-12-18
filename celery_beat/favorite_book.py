# -*- coding:utf-8 -*-
# favorite_book.py


'''
在文献搜索系统的主页，用户可以查到当前一小时内最热门的十大文献，并且能够直接访问该文献。
该文献管理系统所管理的文献数量非常多，达到 PB 的级别。处于用户体验的考虑，用户获得十大
热门文献这个动作需要在较短时间内获得反馈。
'''
from celery import Celery
import time

app = Celery('select_populate_book', backend='rpc://', broker='amqp://localhost')
app.config_from_object('config')


@app.task
def select_populate_book():
    print 'Start to select_populate_book task at {0}'.format(time.ctime())
    time.sleep(2)
    print 'Task select_populate_book succeed at {0}'.format(time.ctime())
    return True

