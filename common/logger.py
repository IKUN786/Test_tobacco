# 日志封装
import logging
import os.path
import time
class infoFilter(logging.Filter):
    """信息日志过滤器：只保留 INFO 级别的日志"""
    def filter(self,record):
        # 只返回 INFO 级别日志
        return record.levelno == logging.INFO
class errFilter(logging.Filter):
    """错误日志过滤器：只保留 ERROR 级别的日志"""
    def filter(self,record):
        # 只返回 ERROR 级别日志
        return record.levelno == logging.ERROR
class logger:
    """日志工具类"""
    """
    @classmethod
    : 这是一个装饰器，用于将下面的getlog方法定义为类方法。
    """
    """
    区别：普通方法的第一个参数通常是 self（代表实例对象），
    而类方法的第一个参数是 cls（代表类本身）。
    这意味着你可以直接通过 logger.getlog() 来调用这个方法，
    而不需要先创建类的实例（即不需要 obj = logger()）。
    """
    @classmethod
    def getlog(cls):
        # 创建日志对象
        cls.logger = logging.getLogger(__name__)
        # 设置日志级别
        cls.logger.setLevel(logging.DEBUG)
        # 获取项目根目录
        LOG_PATH = "../logs/"
        # 判断日志目录是否存在，如果不存在则创建
        if not os.path.exists(LOG_PATH):
            os.mkdir(LOG_PATH)

        # 按日期创建日志文件名
        now = time.strftime("%Y-%m-%d", time.localtime())

        log_name = LOG_PATH + now + ".logs"  # 所有日志
        info_log_name = LOG_PATH + now + "-info.logs"    # 信息日志
        err_log_name = LOG_PATH + now + "-err.logs"  # 错误日志
        # 创建文件处理器
        all_hanlder = logging.FileHandler(log_name,encoding="utf-8")
        info_hanlder = logging.FileHandler(info_log_name,encoding="utf-8")
        err_hanlder = logging.FileHandler(err_log_name,encoding="utf-8")
        # 创建控制台处理器
        # streamHanlder = logging.StreamHandler()
        # 创建日志格式
        formatter = logging.Formatter(
            "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d)] - %(message)s"
        )
        # 设置处理器格式
        all_hanlder.setFormatter(formatter)
        info_hanlder.setFormatter(formatter)
        err_hanlder.setFormatter(formatter)
        # streamHanlder.setFormatter(formatter)
        # 添加过滤器
        info_hanlder.addFilter(infoFilter())
        err_hanlder.addFilter(errFilter())
        # 添加处理器到日志器
        cls.logger.addHandler(all_hanlder)
        cls.logger.addHandler(info_hanlder)
        cls.logger.addHandler(err_hanlder)
        # cls.logger.addHandler(streamHanlder)

        return cls.logger
"""
日志系统特点：
按日期自动创建日志文件
分类记录（全部/信息/错误）
统一的日志格式
详细的调用信息（文件名、函数名、行号）
"""
# 实例化对象
