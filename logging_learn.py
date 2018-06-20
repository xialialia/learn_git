import logging

logger = logging.getLogger()
# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('test')

# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 定义一个filter
filter = logging.Filter('mylogger')
fh.addFilter(filter)
ch.addFilter(filter)

# logger.addFilter(filter)
logger.addHandler(fh)
logger.addHandler(ch)




logger.setLevel(logging.DEBUG)

logger.debug('logger debug message')
logger.info('mylogger')
logger.warning('logger warning message')
logger.error('logger error message')
logger.critical('logger critical message')