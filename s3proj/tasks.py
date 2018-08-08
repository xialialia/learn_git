from __future__ import absolute_import, unicode_literals
# 没有点就是绝对导入，点表示当前目录下的celery文件
from .celery import app 


@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)

# xialiangdeMacBook-Air:py_codetraining xialiang$ python3
# >>> from s3proj import task2,tasks
# >>> t1 = tasks.xsum.delay([1,3,4,5,7])
# >>> t1.get()
# 20
