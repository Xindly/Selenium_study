# coding:  utf-8
# @Author  : LianXinPeng
# @Time    : 2021/2/23 23:55
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from test_wework.base_page import BasePage


class AddMember(BasePage):

    def add_member(self):
        """
        添加成员页面，实现成员添加
        :return:
        """
        self.find(By.CSS_SELECTOR, '#username').send_keys("测试一号")
        self.find(By.CSS_SELECTOR, "#memberAdd_acctid").send_keys("cesshiyihao")
        self.find(By.CSS_SELECTOR, "#memberAdd_phone").send_keys("11111111111")
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
