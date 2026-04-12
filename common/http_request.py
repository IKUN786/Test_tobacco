# 封装HTTP请求，统一接口调用方式：
import requests
from common.logger import logger

class Request:
    """HTTP请求工具类"""
    log = logger.getlog()

    def __init__(self):
        # 🔥 核心修改1：创建Session会话对象，全局复用
        self.session = requests.Session()
        # 可选：统一设置全局请求头（如Content-Type），所有接口自动生效
        self.session.headers.update({
            "Content-Type": "application/json;charset=utf-8"
        })
    def get(self,url,**kwargs):
        """
        **kwargs 是 Python 函数定义中的一个特殊语法，
        它是 keyword arguments（关键字参数）的缩写。
        简单来说，它的作用是：允许你向函数传入任意数量的“带名字”的参数（
        键值对），并在函数内部将它们打包成一个字典来使用。 为了方便理解，
        我们可以把它和 *args 对比来看： • *args：用来接收无名的参数，
        打包成 元组 (value1, value2)。 • **kwargs：用来接收有名的参数，
        打包成 字典 {'key1': value1, 'key2': value2}。
        :param url:
        :param kwargs:
        :return:
        """
        """GET请求"""
        self.log.info("准备发起get请求,url:" + url)
        self.log.info("接口信息：{}".format(kwargs))
        # session

        r = self.session.get(url = url, **kwargs)
        self.log.info("接口响应状态码：{}".format(r.status_code))
        self.log.info("接口响应内容：{}".format(r.text))

        return r
    def post(self,url,**kwargs):
        """发送POST请求"""
        self.log.info("准备发起post请求,url:" + url)
        self.log.info("接口信息：{}".format(kwargs))
        # session

        r = self.session.post(url = url, **kwargs)
        self.log.info("接口响应状态码：{}".format(r.status_code))
        self.log.info("接口响应内容：{}".format(r.text))

        return r
# 实例化对象

