import time


class Keywords:
    """
    把 WebDriver（浏览器对象）作为参数传进来；
    封装所有可复用的浏览器操作；
    提供一个统一接口给测试用例调用。
    """
    def __init__(self, driver):
        self.driver = driver

    # 核心操作关键字  每个关键字实际上是对应一个步骤
    def open(self, step):
        #打开网址
        self.driver.get(step["data"])

    def click(self, step):
        #点击
        self.driver.find_element(step["by"], step["value"]).click()

    def input(self, step):
        #输入文本
        self.driver.find_element(step["by"], step["value"]).send_keys(step["data"])

    def clear(self, step):
        #清空
        self.driver.find_element(step["by"], step["value"]).clear()


    def wait(self, step):
        #等待
        time.sleep(step["data"])