from __future__ import absolute_import, unicode_literals
from celery.schedules import crontab
from .celery import app  
 
# @app.on_after_configure.connect  # 脚本启动就会执行这个函数
# def setup_periodic_tasks(sender, **kwargs):
#     #   test('hello') every 10 seconds.   每隔10s，就调用test（）函数，.s（）表示传参数
#     sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')
#
#     # Calls test('world') every 30 seconds
#     sender.add_periodic_task(30.0, test.s('world'), expires=10)  # 任务结果保留10s
#
#     # Executes every Monday morning at 7:30 a.m.
#     sender.add_periodic_task(
#         crontab(hour=7, minute=30, day_of_week=1),  # 每周一
#         test.s('Happy Mondays!'),
#     )
#
# @app.task
# def test(arg):
#     print(arg)
# # celery beat,任务调度器，是它给worker发任务
# # xialiangdeMacBook-Air:py_codetraining xialiang$ celery -A s3proj.periodic_tasks beat -l debug


# 上面是通过调用函数添加定时任务，也可以像写配置文件 一样的形式添加， 下面是每30s执行的任务

app.conf.beat_schedule = {
        'add-every-10-seconds': {
        'task': 's3proj.tasks.add',
        'schedule': 10.0,
        'args': (16, 16)
    },
}
app.conf.timezone = 'UTC'



