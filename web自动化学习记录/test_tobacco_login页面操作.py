import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 直接启动Edge（自动识别你项目里的 MicrosoftWebDriver.exe）
driver = webdriver.Edge()
# 测试：打开网页（换成你的前端/后端地址都可以）
driver.get("http://localhost:5174/smoke2/login")
# 打印页面标题，验证成功
print("启动成功！页面标题：", driver.title)
time.sleep(2)
# 定位id为username的元素，并输入用户名
element = driver.find_element(By.ID,"username")
element.send_keys("admin2")
# 定位id为password的元素，并输入密码
element = driver.find_element(By.ID,"password")
element.send_keys("123456")
# 定位id为login的元素，并点击登录
element = driver.find_element(By.CLASS_NAME,"login-button")
element.click()
