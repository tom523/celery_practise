# -*- coding:utf-8 -*-
# 创建 Celery 对象
# notify_friends.py


'''
社交网站的用户在其主页发布了一组新的照片，这条新鲜事需要适时地推送至该用户的所有好友。
该网站的活跃用户有千万级别，在同一时刻会有非常多的“新鲜事推送”任务需要处理，并且每个
用户的好友数会达到 1000+的级别。出于用户体验的考虑，用户发布照片的这个操作需要在较
短时间内得到反馈。
'''

from celery import Celery
import time

app = Celery('notify_friends', backend='rpc://', broker='amqp://localhost')


@app.task
def notify_friends(userId, newsId):
    print 'Start to notify_friends task at {0}, userID:{1} newsID:{2}'.format(time.ctime(), userId, newsId)
    time.sleep(2)
    print 'Task notify_friends succeed at {0}'.format(time.ctime())
    return True

