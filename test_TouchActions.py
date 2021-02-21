#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/19 22:14
# @Author  : Shark
# @Site    : 
# @File    : test_TouchActions.py
# @Software: PyCharm
import time

from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By


class TestTouchAction():
    def setup(self):
        self.driver = webdriver.Firefox(executable_path=r"E:\Driver\firefox_driver\geckodriver.exe")
        self.driver.implicitly_wait(6)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_touchaction_scrollbottom(self):
        # 有待解决.......
        """
        打开chrome,访问百度
        向搜索框中输入‘selenium测试’
        通过TouchAction点击搜索框
        滑动到底部，点击下一页
        关闭浏览器
        :return:
        """
        self.driver.get("http://www.baidu.com")
        ele = self.driver.find_element(By.ID, "kw")
        ele_search = self.driver.find_element(By.ID, "su")
        ele.send_keys("selenium测试")
        action = TouchActions(self.driver)
        action.tap(ele_search)
        # action.perform()

        # action.scroll_from_element(ele, 0, 10000)
        action.perform()
        time.sleep(3)


