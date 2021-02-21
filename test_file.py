# coding:  utf-8
# @Author  : LianXinPeng
# @Time    : 2021/2/21 16:17
from time import sleep

from selenium.webdriver.common.by import By

from Base import Base


class TestFile(Base):
    # 文件上传
    def test_file_upload(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element(By.XPATH, "//*[@id='sttb']/img[1]").click()
        self.driver.find_element(By.ID, "stfile").send_keys(r"D:\Selenium_study\baidu.jpg")
        sleep(6)
