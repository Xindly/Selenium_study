# coding:  utf-8
# @Author  : LianXinPeng
# @Time    : 2021/2/23 23:22
from selenium import webdriver
from selenium.webdriver.common.by import By

from test_wework_login.login import Login
from test_wework_login.register import Register


class Index():
    """
    首页页面PO
    """

    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=r"E:\Driver\firefox_driver\geckodriver.exe")
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(6)

    def goto_register(self):
        """
        点击立即注册
        进入到注册的PO
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        return Register(self.driver)

    def goto_login(self):
        """
        点击企业登录
        进入到企业登录的PO
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR, 'index_top_operation_loginBtn').click()
        return Login(self.driver)
