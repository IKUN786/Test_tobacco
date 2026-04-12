# 首页4个数据测试
import pytest
import allure
from utils.yaml_util import read_yaml
from common.logger import logger
from common import public
# 获取首页上方4个板块数据测试
@allure.feature("首页4个数据")
class TestTobaccoHomepageData:
    path = public.get_data_path("test_tobacco_homepage_data.yml")
    print(path)
    @allure.story("首页4个数据接口")
    @pytest.mark.parametrize("case_data",read_yaml(path)["homepage_data"])
    def test_tobacco_homepage_data_001(self,http_client,login_token,get_config,case_data):
        log = logger.getlog()
        """
        测试首页4个数据接口表单格式
        """
        # 2.提取数据
        case_name = case_data["case_name"]
        api = case_data["api"]
        params = case_data["params"]
        expected = case_data["expected"]
        print(params)
        log.info("用例名称：{}".format(case_name))
        # 3.调用接口
        url = f"{get_config['env']['host']}{api}"
        log.info("请求地址：{}".format(url))
        headers = {"Authorization": f"Bearer {login_token}"}
        response = http_client.get(url,params=params,headers=headers)
        # 4.断言
        assert response.status_code == expected["status_code"]
        assert response.json()["code"] == expected["code"]
        assert response.json()["msg"] == expected["msg"]

