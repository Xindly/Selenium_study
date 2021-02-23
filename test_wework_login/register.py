# coding:  utf-8
# @Author  : LianXinPeng
# @Time    : 2021/2/23 23:27
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Register():
    """
    注册页面PO
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def register(self):
        """
        输入内容
        点击下拉框
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR, '#corp_name').send_keys("测试学院")
        self.driver.find_element(By.CSS_SELECTOR, "#manager_name").send_keys("测试管理员")
        return True
