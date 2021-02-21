# coding:  utf-8
# @Author  : LianXinPeng
# @Time    : 2021/2/21 13:56
import time

from selenium.webdriver.common.by import By

from Base import Base


class TestWindow(Base):

    # 窗口切换
    def test_window(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element(By.LINK_TEXT, "登录").click()
        # 打印当前窗口句柄
        print(self.driver.current_window_handle)
        self.driver.find_element(By.LINK_TEXT, "立即注册").click()
        # 打印当前窗口句柄
        print(self.driver.current_window_handle)

        # 打印浏览器所有的窗口句柄
        print(self.driver.window_handles)

        # 切换浏览器窗口到注册标签页
        windows = self.driver.window_handles
        self.driver.switch_to_window(windows[-1])
        self.driver.find_element(By.ID, "TANGRAM__PSP_4__userName").send_keys("username")
        self.driver.find_element(By.ID,"TANGRAM__PSP_4__phone").send_keys("13111111111")
        time.sleep(5)

        # 再切换回去到第一个标签页,并输入账号密码点击登录
        self.driver.switch_to_window(windows[0])
        self.driver.find_element(By.ID,"TANGRAM__PSP_11__footerULoginBtn").click()
        self.driver.find_element(By.ID,"TANGRAM__PSP_11__userName").send_keys("username")
        self.driver.find_element(By.ID,"TANGRAM__PSP_11__password").send_keys("13111111111")
        self.driver.find_element(By.ID,"TANGRAM__PSP_11__submit").click()
        time.sleep(6)

