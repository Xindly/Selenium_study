# coding:  utf-8
# @Author  : LianXinPeng
# @Time    : 2021/2/23 23:53

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from test_wework.add_member import AddMember
from test_wework.base_page import BasePage


class Index(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_add_member(self):
        """
        添加成员
        :return:
        """

        def add_member_condition(x):
            """
            改写显示等待条件
            :param x:
            :return:
            """
            elements_len = len(self.finds(By.CSS_SELECTOR, "#username"))
            if elements_len <= 0:
                self.find(By.CSS_SELECTOR, ".js_has_member>div:nth-child(1)>a:nth-child(2)").click()
            return elements_len > 0

        self.find(By.CSS_SELECTOR, "#menu_contacts").click()
        self.wait_for_condition(add_member_condition)

        return AddMember(self._driver)

    def goto_import_address(self):
        """
        导入通讯录
        :return:
        """
        pass

    def goto_join_member(self):
        """
        成员加入
        :return:
        """
        pass
