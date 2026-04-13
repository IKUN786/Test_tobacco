from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login():
    # 初始化Chrome浏览器
    driver = webdriver.Chrome()
    # 设置显式等待，最多等待10秒
    wait = WebDriverWait(driver, 10)

    try:
        # 访问登录页
        driver.get("http://novel.hctestedu.com/user/login.html")

        # 等待用户名输入框出现并输入
        username_input = wait.until(EC.presence_of_element_located((By.ID, "txtUName")))
        username_input.send_keys("15574113907")

        # 等待密码框出现并输入
        password_input = wait.until(EC.presence_of_element_located((By.NAME, "txtPassword")))
        password_input.send_keys("123456")

        # 等待登录按钮可点击并点击
        login_btn = wait.until(EC.element_to_be_clickable((By.ID, "btnLogin")))
        login_btn.click()

        # 断言登录成功
        assert "欢迎" in driver.page_source
        print("登录测试通过!")

    finally:
        # 无论测试成功/失败，都关闭浏览器
        driver.quit()


# 运行测试
if __name__ == "__main__":
    test_login()