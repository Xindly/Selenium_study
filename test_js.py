# coding:  utf-8
# @Author  : LianXinPeng
# @Time    : 2021/2/21 14:50
from time import sleep

from selenium.webdriver.common.by import By

from Base import Base


class TestJS(Base):
    def test_js_scroll(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element(By.ID, "kw").send_keys("selenium测试")
        # 执行js语句；要想有返回，需要return
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
        sleep(6)
        # 向下移动
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        sleep(5)
        self.driver.find_element(By.XPATH, "//*[@id='page']/div/a[10]").click()
        sleep(5)

    # 时间控件
    def test_datetime(self):
        self.driver.get("https://www.12306.cn/")
        # 执行多个js语句;中间用分号隔开
        time_ele = self.driver.execute_script("a = document.getElementById('train_date');a.removeAttribute('readonly')")
        self.driver.execute_script("document.getElementById('train_date').value='2021-12-30'")
        print(self.driver.execute_script("return document.getElementById('train_date').value"))
        sleep(5)