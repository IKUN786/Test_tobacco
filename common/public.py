# 常用路径等操作封装
import os

# 动态获取项目根目录（自动适配，无硬编码）
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
class Public:
    @staticmethod
    def get_data_path(filename):
        """获取data目录下文件路径"""
        return os.path.join(BASE_DIR, "data", filename)

    @staticmethod
    def get_config_path(filename):
        """获取config目录下文件路径"""
        return os.path.join(BASE_DIR, "config", filename)
# 🔥 关键修复：创建实例，让你直接调用
public = Public()