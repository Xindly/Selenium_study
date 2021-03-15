# coding:  utf-8
# @Author  : LianXinPeng
# @Time    : 2021/3/3 22:40
from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By


class TestBrowser():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['browserName'] = "Browser"
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['noReset'] = True
        desired_caps['cheomedriverExcutable'] = r'E:\Driver\chrome_driver\chromedriver20.exe'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        sleep(10)
        self.driver.quit()

    def test_browser(self):
        self.driver.get("http://m.baidu.com")
        self.driver.find_element(By.ID,"index-kw").click()
        self.driver.find_element(By.ID,"index-kw").send_keys("appium")
        self.driver.find_element(By.ID,"index-bn").click()

