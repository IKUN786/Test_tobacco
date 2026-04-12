# pytest自定义命令行参数，切换环境
import os
import pytest
from common.http_request import Request
from utils.yaml_util import read_yaml
import common
from common import public
import allure
@pytest.fixture(scope="session")
def get_config():

    path = common.public.get_config_path("config.yml")
    print(path)
    return read_yaml(path)

@pytest.fixture(scope="session")
def http_client():
    return Request()
# 自动添加Allure环境信息
@pytest.fixture(scope="session", autouse=True)
def set_allure_env(get_config):
    # 动态获取项目次级根目录（自动适配，无硬编码）
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(BASE_DIR, "report","allure-results","environment.properties")

    with open(path, "w", encoding="utf-8") as f:
        f.write(f"Host={get_config['env']['host']}\n")
@pytest.fixture(scope="session")
def login_token(http_client, get_config):
    """登录并返回 token"""
    path = public.get_data_path("test_tobacco_sucess_login.yml")
    data = read_yaml(path)["test_login"][0]
    url = f"{get_config['env']['host']}{data['login_api']}"
    resp = http_client.post(url, json=data["body"])
    assert resp.status_code == data["expected"]["status_code"]
    assert resp.json()["code"] == data["expected"]["code"]
    token = resp.json().get("data", {}).get("token")  # 根据实际响应结构调整
    return token