# coding:  utf-8
# @Author  : LianXinPeng
# @Time    : 2021/2/26 23:15
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from hamcrest import *
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
        # pass
        sleep(10)
        self.driver.quit()

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

    def test_my_login(self):
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, "new UiSelector().text('我的')").click()

        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我的")').click()
        # 组合定位
        id_text = 'resourceId("com.xueqiu.android:id/tab_name").text("我的")'
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, id_text).click()

        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, "new UiSelector().textContains('账号密码')").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("密码登录")').click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiSelector().resourceId("com.xueqiu.android:id/login_account")'). \
            send_keys("17311111111")
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiSelector().resourceId("com.xueqiu.android:id/login_password")'). \
            send_keys("111111")
        # self.driver.find_element(
        #     MobileBy.ANDROID_UIAUTOMATOR('new UiSelector().resourceId("com.xueqiu.android:id/button_next")')).click()

        class_text = 'className("android.widget.TextView").textContains("快捷登录")'
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, class_text).click()

    def test_guanxidingwei(self):
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search").click()
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/name").click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='股票']").click()
        # 先找到父节点，再找到子节点
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiSelector().resourceId("com.xueqiu.android:id/title_container")'
                                 '.childSelector(text("股票"))').click()
        # hk_price = self.driver.find_element(MobileBy.XPATH,
        #                                     "//*[@text='09988']/../../..//*[contains(@resource-id,'current_price')]").text

        locator = (MobileBy.XPATH, "//*[@text='09988']/../../..//*[contains(@resource-id,'current_price')]")
        # locator = (MobileBy.XPATH, "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price')]")
        # ele = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))

        # lamba表达式
        ele = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*locator))
        self.driver.find_element(*locator)
        print(ele.text)
        hk_price = float(ele.text)
        assert hk_price > 200

    # 滚动查找元素
    def test_uiscroll(self):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector().text("1小时前").instance(0));').click()

    def test_haemcrest(self):
        assert_that(10, equal_to(9), "这是一个提示")
