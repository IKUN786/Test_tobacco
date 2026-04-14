# test_edge.py
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# 直接启动Edge（自动识别你项目里的 MicrosoftWebDriver.exe）
driver = webdriver.Edge()
# 测试：打开网页（换成你的前端/后端地址都可以）
driver.get("https://www.baidu.com/")
# 打印页面标题，验证成功
print("启动成功！页面标题：", driver.title)
time.sleep(2)
# 定位元素，输入用户名和密码
element = driver.find_element(By.LINK_TEXT, "新闻")
element.click()
time.sleep(2)
driver.get("https://www.bilibili.com/")
time.sleep(2)
element = driver.find_element(By.PARTIAL_LINK_TEXT, "番剧")
time.sleep(4)
element.click()
time.sleep(5)
driver.close()
driver.quit()
