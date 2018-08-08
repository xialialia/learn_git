from celery import Celery
import time
# 当有多个worker的时候是抢任务
# amqp指的是连接的是rabbitmq
app = Celery('tasks',  # app的名字
             broker='redis://127.0.0.1:6379/5',
             backend='redis://127.0.0.1:6379/6'  # 把结果写到redis里面
      )


@app.task
def add(x, y):
    print("running...", x, y)
    return x + y

@app.task
def cmd(cmd_str):
    print("running...", cmd_str)
    time.sleep(10)
    return time.time()

