# coding:  utf-8
# @Author  : LianXinPeng
# @Time    : 2021/2/23 23:55
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class AddMember():
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def add_member(self):
        self.driver.find_element(By.CSS_SELECTOR, '#username').send_keys("测试一号")
        self.driver.find_element(By.CSS_SELECTOR, "#memberAdd_acctid").send_keys("测试一号")
        self.driver.find_element(By.CSS_SELECTOR, "#memberAdd_phone").send_keys("11111111111")
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
