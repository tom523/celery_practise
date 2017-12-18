

#### change a single setting
```
app.conf.task_serializer = 'json'
```

#### change many single settings
```
app.conf.update(
    task_serializer='json',
    accept_content=['json'],  # Ignore other content
    result_serializer='json',
    timezone='Europe/Oslo',
    enable_utc=True,
)
```
#### using a dedicated configuration module
```
app.config_from_object('celeryconfig')
```
celeryconfig.py:
```
broker_url = 'pyamqp://'
result_backend = 'rpc://'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Europe/Oslo'
enable_utc = True
```



