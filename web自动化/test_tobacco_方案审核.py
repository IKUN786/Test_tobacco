import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 直接启动Edge（自动识别你项目里的 MicrosoftWebDriver.exe）
driver = webdriver.Edge()
wait = WebDriverWait(driver, 20)  # 延长等待时间
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
time.sleep(2)
element = driver.find_element(By.XPATH,"//div[contains(text(), '审核流程')]")
element.click()
time.sleep(1)
element = driver.find_element(By.XPATH,"//a[contains(text(), '方案管理')]")
element.click()
time.sleep(1)
element = driver.find_element(By.XPATH,"//div[@id='app']/main/div/div[2]/div/div/div/div[3]/div/div/div/table/tbody/tr[3]/td[8]/div/button")
element.click()
time.sleep(1)
element = driver.find_element(By.XPATH,"//button[contains(.,'进行审核')]")
element.click()
time.sleep(1)
element = driver.find_element(By.XPATH,"//span/button[2]")
element.click()
