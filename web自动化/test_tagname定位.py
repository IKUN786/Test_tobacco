# test_edge.py
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# 直接启动Edge（自动识别你项目里的 MicrosoftWebDriver.exe）
driver = webdriver.Edge()
# 测试：打开网页（换成你的前端/后端地址都可以）
driver.get("https://www.bilibili.com/")
# 打印页面标题，验证成功
print("启动成功！页面标题：", driver.title)
time.sleep(2)
# 定位用户名输入框，输入用户名
element = driver.find_element(By.TAG_NAME, 'input')
element.send_keys("学习selenium")
time.sleep(2)

# 不推荐
# element = driver.find_element(By.TAG_NAME, 'input')[50].click()

element = driver.find_element(By.CSS_SELECTOR,".nav-search-btn > svg")
element.click()
time.sleep(2)
driver.close()
driver.quit()