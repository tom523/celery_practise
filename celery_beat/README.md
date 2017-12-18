# celery beat的使用

##### 参考文档：[利用 Celery 构建 Web 服务的后台任务调度模块](https://www.ibm.com/developerworks/cn/opensource/os-cn-celery-web-service/index.html)

### 创建一个简单的celery任务
##### 运行Celery Worker
```
celery -A notify_friends worker --loglevel=info
```
##### 触发notify_friends任务
```
$ python call_notify_friends.py
```

### 利用调度器创建周期任务
##### 运行worker
```
celery -A favorite_book worker --loglevel=info
```
##### 启动celery beat
```
celery -A favorite_book beat -l info
```
