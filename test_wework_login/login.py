# coding:  utf-8
# @Author  : LianXinPeng
# @Time    : 2021/2/23 23:25
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from test_wework_login.register import Register


class Login():
    """
    登录页面的PO
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def scan(self):
        """
        扫描二维码
        :return:
        """
        pass

    def goto_register(self):
        """
        点击立即注册
        进入到注册的PO
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR, '.login_registerBar_link').click()
        return Register(self.driver)
