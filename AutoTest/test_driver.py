from selenium import webdriver
import time


class Test:
    def __init__(self):
        self.driver = webdriver.Chrome()  # 注意Chrome的C是大写，
        # wecdiver.exe文件放在环境变量下可能没有用放在Python安装目录下Script目录下

    def test_driver(self):
        self.driver.get("https://www.baidu.com")
        self.driver.implicitly_wait(3)  # 隐士等待
        self.driver.find_element_by_link_text("贴吧").click()
        time.sleep(5)  # 显示等待

    def test_quit(self):
        self.driver.quit()


if __name__ == "__main__":
    test = Test()
    test.test_driver()
    test.test_quit()