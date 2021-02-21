# coding:  utf-8
# @Author  : LianXinPeng
# @Time    : 2021/2/21 13:58
import os

from selenium import webdriver


class Base():
    def setup(self):
        # browser = os.getenv("browser")
        # if browser == "firefox":
        #     self.driver = webdriver.Firefox(executable_path=r"E:\Driver\firefox_driver\geckodriver.exe")
        # elif browser == "headless":
        #     self.driver = webdriver.PhantomJS()
        # else:
        #     self.driver = webdriver.Chrome()
        self.driver = webdriver.Firefox(executable_path=r"E:\Driver\firefox_driver\geckodriver.exe")
        self.driver.implicitly_wait(6)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()
