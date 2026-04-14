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
element = driver.find_element(By.NAME, "username")
element.send_keys("admin")