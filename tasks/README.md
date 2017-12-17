```
tom@tom-VirtualBox:/tmp/proj$ sudo lsb_release -a
[sudo] password for tom: 
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 16.04.3 LTS
Release:	16.04
Codename:	xenial
```

```
$ sudo apt-get install rabbitmq-server
```

```
$ pip install celery
```

#### Running the Celery worker server
```
$ celery -A tasks worker -l info
```

另外启动一个terminal，Calling the task

```
>>> from tasks import add
>>> result = add.delay(4, 4)
>>> result.ready()
False
>>> result.get(timeout=1)
8
>>> result.get(propagate=False)
>>> result.traceback
?
```
