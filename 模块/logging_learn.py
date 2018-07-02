import time

import loggin_module      # 导入自定义的logging配置
import logging


logger = logging.getLogger(__name__)  # 生成logger实例,__name__是logger实例的名字


def demo():
    logger.debug("start range... time:{}".format(time.time()))
    logger.info("中文测试开始。。。")
    logger.info(__name__)
    for i in range(10):
        logger.debug("i:{}".format(i))
        time.sleep(0.2)
    else:
        logger.debug("over range... time:{}".format(time.time()))
    logger.info("中文测试结束。。。")

if __name__ == "__main__":
    loggin_module.load_my_logging_cfg()  # 在你程序文件的入口加载自定义logging配置
    demo()