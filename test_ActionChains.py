#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/19 21:26
# @Author  : Shark
# @Site    : 
# @File    : test_ActionChains.py
# @Software: PyCharm
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Firefox(executable_path=r"E:\Driver\firefox_driver\geckodriver.exe")
        self.driver.implicitly_wait(6)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element(By.XPATH, "//input[@value='click me']")
        element_doubleclick = self.driver.find_element(By.XPATH, "//input[@value='dbl click me']")
        element_rightclick = self.driver.find_element(By.XPATH, "//input[@value='right click me']")
        action = ActionChains(self.driver)
        action.click(element_click)
        action.double_click(element_doubleclick)
        action.context_click(element_rightclick)
        time.sleep(5)
        action.perform()
        time.sleep(5)

    def test_moveto_element(self):
        self.driver.get("http://www.baidu.com")
        ele = self.driver.find_element(By.ID, "s-usersetting-top")
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        time.sleep(3)

    # 拖拽的三种用法
    def test_drag_drop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_element = self.driver.find_element(By.ID, "dragger")
        drop_element = self.driver.find_element(By.XPATH, "/html/body/div[2]")
        action = ActionChains(self.driver)
        # action.drag_and_drop(drag_element, drop_element)
        # action.click_and_hold(drag_element).release(drop_element)
        action.click_and_hold(drag_element).move_to_element(drop_element).release()
        action.perform()
        time.sleep(3)

    # 模拟键盘操作
    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele = self.driver.find_element(By.XPATH, "/html/body/label[1]/input").click()
        actions = ActionChains(self.driver)
        actions.send_keys("username").pause(2)    # pause等待
        actions.send_keys(Keys.SPACE).pause(2)    # 空格
        actions.send_keys("tom").pause(2)
        actions.send_keys(Keys.BACK_SPACE).perform()   # 删除
        time.sleep(3)
