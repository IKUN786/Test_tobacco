# 登录封装
import pytest
import allure
from utils.yaml_util import read_yaml
from common.logger import logger
from common import public
# 登录测试
@allure.feature("登录模块")
class TestLogin:
    path = public.get_data_path("test_tobacco_login_data.yml")
    print(path)
    @allure.story("登录接口")
    @pytest.mark.parametrize("case_data",read_yaml(path)["test_login"])
    def test_login(self,http_client,get_config, case_data):
        log = logger.getlog()
        """
        测试登录接口（Body JSON 格式）
        """
        # 2.提取数据
        case_name = case_data["case_name"]
        request_body = case_data["body"]
        print(request_body)
        expected = case_data["expected"]
        api = case_data["login_api"]
        log.info("用例名称：{}".format(case_name))
        # 3.调用接口
        # 推荐
        url = f"{get_config['env']['host']}{api}"
        response = http_client.post(url,json=request_body)
        # 4.断言
        assert response.status_code == expected["status_code"]
        assert response.json()["code"] == expected["code"]