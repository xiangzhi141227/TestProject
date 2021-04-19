from selenium import webdriver
import time


class Test:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def test_driver(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_link_text("贴吧").click()
        time.sleep(5)

    def test_quit(self):
        self.driver.quit()


if __name__ == "__main__":
    test = Test()
    test.test_driver()
    test.test_quit()