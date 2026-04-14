# test_edge.py
import time

from selenium import webdriver
# 直接启动Edge（自动识别你项目里的 MicrosoftWebDriver.exe）
driver = webdriver.Edge()
# 测试：打开网页（换成你的前端/后端地址都可以）
driver.get("http://localhost:5174/smoke2/login")
time.sleep(2)
# 浏览器打开的位置
driver.set_window_position(500,100)
# 浏览器打开的尺寸
driver.set_window_size(800,600)
# 浏览器最大化
driver.maximize_window()
time.sleep(2)
# 最小化
driver.minimize_window()
time.sleep(2)
# 最大化
driver.maximize_window()
# 打印页面标题，验证成功
print("启动成功！页面标题：", driver.title)
