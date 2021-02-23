# coding:  utf-8
# @Author  : LianXinPeng
# @Time    : 2021/2/23 21:40
from time import sleep

from selenium.webdriver.common.by import By

from Base import Base


class TestCookie(Base):
    def test_cookie(self):
        self.driver.get("https://work.weixin.qq.com/")
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        print(self.driver.get_cookies())
        # cookies = self.driver.get_cookies()
        cookies = [{'name': 'wwrtx.c_gdpr', 'value': '0', 'path': '/', 'domain': '.work.weixin.qq.com', 'secure': False, 'httpOnly': False, 'expiry': 1645626329, 'sameSite': 'None'}, {'name': 'ww_rtkey', 'value': '41mii2e', 'path': '/', 'domain': 'work.weixin.qq.com', 'secure': False, 'httpOnly': True, 'expiry': 1614121865, 'sameSite': 'None'}, {'name': 'wwrtx.ref', 'value': 'direct', 'path': '/', 'domain': '.work.weixin.qq.com', 'secure': False, 'httpOnly': True, 'sameSite': 'None'}, {'name': 'wwrtx.refid', 'value': '13993460341527600', 'path': '/', 'domain': '.work.weixin.qq.com', 'secure': False, 'httpOnly': True, 'sameSite': 'None'}, {'name': 'wwrtx.i18n_lan', 'value': 'zh', 'path': '/', 'domain': '.work.weixin.qq.com', 'secure': False, 'httpOnly': False, 'expiry': 1616682329, 'sameSite': 'None'}]

        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
                self.driver.add_cookie(cookie)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
