import time

from selenium import webdriver
fuck = webdriver.Edge()
fuck.get("http://localhost:5174/smoke2/login")
time.sleep(2)
# 浏览器截图
fuck .get_screenshot_as_file("浏览器截图.png")
time.sleep(3)
# 刷新网页
fuck.refresh()