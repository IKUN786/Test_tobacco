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
time.sleep(3)
# driver.find_elements(By.CSS_SELECTOR, '.channel-link')[0].click()
# element = driver.find_element(By.CSS_SELECTOR, '#app > div.bili-feed4 > div.bili-header.large-header > div.bili-header__channel > div.right-channel-container > div.channel-items__left > a:nth-child(1)')
# 模糊匹配
element = driver.find_elements(By.CSS_SELECTOR, "a[href*='anime']")
element[1].click()
time.sleep(4)
driver.close()
driver.quit()
