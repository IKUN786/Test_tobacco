
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 直接启动Edge（自动识别你项目里的 MicrosoftWebDriver.exe）
driver = webdriver.Edge()
# 打开网址
driver.get("http://localhost:5174/smoke2/login")
# 初始化等待，页面渲染完成
wait = WebDriverWait(driver, 10)

# 定位用户名输入框，输入用户名
username_input = wait.until(EC.presence_of_element_located((By.ID, "username")))
username_input.send_keys("admin")
print("用户名输入成功！")
# 定位密码输入框，输入密码
username_input = wait.until(EC.presence_of_element_located((By.ID, "password")))
username_input.send_keys("123456")
print("密码输入成功！")
# 定位登录按钮，点击登录
login_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "login-button")))
login_button.click()
print("登录成功！")
# 关闭浏览器
driver.quit()

