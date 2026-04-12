import os
from pathlib import Path

import yaml
# 管理测试数据，实现数据持久化：
# 🔥 自动获取项目根目录（全框架统一，不会变）
def write_yaml(filename,data):
    """往yml中写数据"""
    with open(filename,mode="a+",encoding="utf-8") as f:
        """将 Python 对象data（字典/列表）安全地转换成 YAML 格式，
        并写入到文件 f 中。"""
        yaml.safe_dump(data,stream=f)

def read_yaml(filename,key=None):
    """从yml中读数据"""
    with open(filename,mode="r",encoding="utf-8") as f:
        """从文件 f 中读取 YAML 格式的内容，转换成 Python 对象，
        然后返回该对象中指定 key 对应的值。"""
        data = yaml.safe_load(f)
        if key:
            return data[key]
        else:
            return data
def clear_yaml(filename):
    """清空yml文件"""
    with open(filename,mode="w",encoding="utf-8") as f:
        f.truncate()

