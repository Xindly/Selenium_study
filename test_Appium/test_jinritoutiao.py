# coding:  utf-8
# @Author  : LianXinPeng
# @Time    : 2021/3/6 16:50
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By


class TestJinriToutiao():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = '793QBDR6229XK'
        desired_caps['appPackage'] = 'com.ss.android.article.news'
        desired_caps['appActivity'] = '.activity.MainActivity'
        desired_caps['automationName'] = 'UiAutomator2'
        # 'automationName=UiAutomator2'
        # com.ss.android.article.news.activity.MainActivity /.activity.MainActivity
        desired_caps['noReset'] = True
        desired_caps['unicodeKeyBoard'] = True
        desired_caps['resetKeyBoard'] = True
        desired_caps['dontStopAppOnReset'] = True
        desired_caps['newCommandTimeout'] = 6000
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        # pass
        sleep(10)
        self.driver.quit()

    def test_one1(self):
        print(self.driver.contexts)
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, '关注').click()
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@resource-id,'com.ss.android.article.news:id/dpt')]").click()
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@resource-id='com.ss.android.article.news:id/a']"
                                 "/*[@resource-id='com.ss.android.article.news:id/dqs']").send_keys("魅族")
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@resource-id='com.ss.android.article.news:id/ccu']"
                                 "/*[@class='android.widget.FrameLayout']"
                                 "/*[@class='android.view.ViewGroup']"
                                 "/*[@class='android.view.ViewGroup']").click()

        sleep(5)
