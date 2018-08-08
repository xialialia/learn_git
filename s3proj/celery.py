from __future__ import absolute_import, unicode_literals
# 从python安装 包的绝对路径里去import， 而不是从当前目录import
from celery import Celery
 
app = Celery('proj',
             broker='redis://127.0.0.1:6379/5',
             backend='redis://127.0.0.1:6379/6',
             include=['s3proj.tasks', "s3proj.task2", "s3proj.periodic_tasks"])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)
 
if __name__ == '__main__':
    app.start()

# xialiangdeMacBook-Air:py_codetraining xialiang$ celery -A s3proj worker -l debug
