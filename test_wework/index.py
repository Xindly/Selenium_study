# coding:  utf-8
# @Author  : LianXinPeng
# @Time    : 2021/2/23 23:53

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from test_wework.add_member import AddMember


class Index():
    def __init__(self):
        chrome_options = Options()
        chrome_options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(executable_path=r"E:\Driver\chrome_driver\chromedriver.exe",
                                       options=chrome_options)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.implicitly_wait(5)

    def goto_add_member(self):
        """
        添加成员
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap").click()
        return AddMember(self.driver)

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
