from __future__ import absolute_import, unicode_literals
# 没有点就是绝对导入，点表示当前目录下的celery文件
from .celery import app


@app.task
def cdm(x):
    return x


