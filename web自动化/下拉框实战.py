from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.get('http://60.204.225.104/login?redirect=%2Freport%2Fdeliver')
# 打印页面标题，验证成功
print("启动成功！页面标题：", driver.title)
time.sleep(2)
# 定位id为username的元素，并输入用户名
element = driver.find_element(By.XPATH,"//input[@placeholder='账号']")
element.send_keys("admin")

# 定位id为password的元素，并输入密码
element = driver.find_element(By.XPATH,"//input[@placeholder='密码']")
element.send_keys("123456")

element = driver.find_element(By.XPATH,"//input[@placeholder='验证码']")
element.send_keys("2")
element = driver.find_element(By.XPATH,"//button[contains(.,'登 录')]")
element.click()
time.sleep(10)
# select = Select(driver.find_element(By.CLASS_NAME, 'dropdown-menu'))
# select.select_by_value('2')
