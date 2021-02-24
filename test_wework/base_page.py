# coding:  utf-8
# @Author  : LianXinPeng
# @Time    : 2021/2/24 22:01
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage():
    _driver = None
    _base_url = ""

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            chrome_options = Options()
            chrome_options.debugger_address = "127.0.0.1:9222"
            self._driver = webdriver.Chrome(executable_path=r"E:\Driver\chrome_driver\chromedriver.exe",
                                            options=chrome_options)
            self._driver.implicitly_wait(5)
        else:
            self._driver = driver

        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self, by, locator):
        return self._driver.find_element(by, locator)
