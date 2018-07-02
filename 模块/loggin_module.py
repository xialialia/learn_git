# import logging
# logging.basicConfig(filename='access.log',
#                     format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S %p',
#                     level=20)
#
# logging.debug('调试debug')
# logging.info('消息info')
# logging.warning('警告warn')
# logging.error('错误error')
# logging.critical('严重critical')

# import logging
#
# #1、logger对象：负责产生日志，然后交给Filter过滤，然后交给不同的Handler输出
# logger=logging.getLogger(__file__)
#
# #2、Filter对象：不常用，略
#
# #3、Handler对象：接收logger传来的日志，然后控制输出
# h1=logging.FileHandler('t1.log') #打印到文件
# h2=logging.FileHandler('t2.log') #打印到文件
# h3=logging.StreamHandler() #打印到终端
#
# #4、Formatter对象：日志格式
# formmater1=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S %p',)
#
# formmater2=logging.Formatter('%(asctime)s :  %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S %p',)
#
# formmater3=logging.Formatter('%(name)s %(message)s',)
#
#
# #5、为Handler对象绑定格式
# h1.setFormatter(formmater1)
# h2.setFormatter(formmater2)
# h3.setFormatter(formmater3)
#
# #6、将Handler添加给logger并设置日志级别
# logger.addHandler(h1)
# logger.addHandler(h2)
# logger.addHandler(h3)
# logger.setLevel(10)
#
# #7、测试
# logger.debug('debug')
# logger.info('info')
# logger.warning('warning')
# logger.error('error')
# logger.critical('critical')

# import logging
#
#
# form=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S %p',)
#
# ch=logging.StreamHandler()
#
# ch.setFormatter(form)
# # ch.setLevel(10)
# ch.setLevel(30)
#
# l1=logging.getLogger('root')  # logger是第一级过滤，然后才能到handler
# # l1.setLevel(20)
# l1.setLevel(20)
# l1.addHandler(ch)
#
# l1.debug('debug')
# l1.info('info')
# l1.warning('warning')
# l1.error('error')
# l1.critical('critical')


# import os
# a= os.path.dirname(os.path.abspath(__file__))
# print(a)
# print(os.path.dirname(os.path.abspath(__file__)), os.path.abspath(__file__))
# print(os.path.isdir(r'/Users/xialiang/PycharmProjects/py_codetraining/模块/loggin_module.py'))

# filter 用法
# import logging
#
# logger = logging.getLogger('xialiang')
# # 创建一个handler，用于写入日志文件
# fh = logging.FileHandler('test.log')
#
# # 再创建一个handler，用于输出到控制台
# ch = logging.StreamHandler()
#
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
# fh.setFormatter(formatter)
# ch.setFormatter(formatter)
#
# # 定义一个filter
# filter = logging.Filter('xialiang')
# fh.addFilter(filter)
# ch.addFilter(filter)
#
# # logger.addFilter(filter)
# logger.addHandler(fh)
# logger.addHandler(ch)
#
#
# logger.setLevel(logging.DEBUG)
#
# logger.debug('logger debug message')
# logger.info('logger info message')
# logger.warning('logger warning message')
# logger.error('logger error message')
# logger.critical('logger critical message')
#
# ##################################################
# logger1 = logging.getLogger('mylogger')
# logger1.setLevel(logging.DEBUG)
#
# logger2 = logging.getLogger('mylogger')
# logger2.setLevel(logging.INFO)
#
# logger1.addHandler(fh)
# logger1.addHandler(ch)
#
# logger2.addHandler(fh)
# logger2.addHandler(ch)
#
# logger1.debug('logger1 debug message')
# logger1.info('logger1 info message')
# logger1.warning('logger1 warning message')
# logger1.error('logger1 error message')
# logger1.critical('logger1 critical message')
#
# logger2.debug('logger2 debug message')
# logger2.info('logger2 info message')
# logger2.warning('logger2 warning message')
# logger2.error('logger2 error message')
# logger2.critical('logger2 critical message')







# ----------------------------------------------------
import os, sys
import logging.config

a = os.path.abspath(__file__)
sys.path.append(a)

# 定义三种日志输出格式 开始

standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]' #其中name为getlogger指定的名字

simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'

id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'

# 定义日志输出格式 结束

logfile_dir = os.path.dirname(os.path.abspath(__file__))  # log文件的目录

logfile_name = 'all2.log'  # log文件名

# 如果不存在定义的日志目录就创建一个
if not os.path.isdir(logfile_dir):
    os.mkdir(logfile_dir)

# log文件的全路径
logfile_path = os.path.join(logfile_dir, logfile_name)

# log配置字典
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
    },
    'filters': {},
    'handlers': {
        #打印到终端的日志
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        #打印到文件的日志,收集info及以上的日志
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'standard',
            'filename': logfile_path,  # 日志文件
            'maxBytes': 1024*1024*5,  # 日志大小 5M
            'backupCount': 5,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
    },
    'loggers': {
        #logging.getLogger(__name__)拿到的logger配置
        '': {
            'handlers': ['default', 'console'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',
            # 如果此属性的计算结果为true，除了附加到此记录器的任何处理程序外，记录到此记录程序的事件将传递给更高级别（祖先）记录程序的处理程序。消息直接传递给祖先记录器的处理程序 - 既不考虑祖先记录器的级别也不考虑过滤器。
            'propagate': True,  # 向上（更高level的logger）传递
        },
    },
}


def load_my_logging_cfg():
    logging.config.dictConfig(LOGGING_DIC)  # 导入上面定义的logging配置
    # logger = logging.getLogger(__name__)# 生成一个log实例
    # a=__name__
    # logger.info(a)  # 记录该文件的运行状态

if __name__ == '__main__':
    load_my_logging_cfg()
