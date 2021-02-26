# coding:  utf-8
# @Author  : LianXinPeng
# @Time    : 2021/2/26 23:15
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestXueqiu():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
        desired_caps['noReset'] = True
        desired_caps['unicodeKeyBoard'] = True
        desired_caps['resetKeyBoard'] = True
        desired_caps['dontStopAppOnReset'] = True
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        pass
        # sleep(10)
        # self.driver.quit()

    # def wait(self):
    #     WebDriverWait(self.driver).until(expected_conditions.visibility_of_element_located())

    def test_search(self):
        # self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        # self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")

        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search").click()
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")

    def test_search_and_get_price(self):
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search").click()
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/name").click()
        print(self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/current_price").text)
        assert float(self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/current_price").text) > 200

    def test_scroll(self):
        """
        向上滑动
        long_press  长按
        :return:
        """
        size = self.driver.get_window_rect()
        for i in range(10):
            TouchAction(self.driver).long_press(x=size['width'] * 0.5, y=size['height'] * 0.8).move_to(
                x=size['width'] * 0.5, y=size['height'] * 0.2).release().perform()

    def test_xpath(self):
        """
        输入alibaba，找到香港的股票价格
        :return:
        """
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search").click()
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/name").click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='股票']").click()
        hk_price = self.driver.find_element(MobileBy.XPATH,
                                            "//*[@text='09988']/../../..//*[contains(@resource-id,'current_price')]").text
        print(hk_price)
        assert float(hk_price) > 240

    def test_device(self):
        # 把app放在后台6秒
        self.driver.background_app(6)
