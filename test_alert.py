# coding:  utf-8
# @Author  : LianXinPeng
# @Time    : 2021/2/21 16:35
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Base import Base


class TestAlert(Base):
    def test_alert(self):
        """
        打开网页（https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable）
        操作窗口右侧页面，将元素1拖拽到元素2
        点击alert弹框中的确定
        点击运行，关闭页面
        :return:
        """
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        drag = self.driver.find_element(By.ID, "draggable")
        drop = self.driver.find_element(By.ID, "droppable")
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()
        sleep(3)

        print("点击alert确认")
        print(self.driver.switch_to.alert.text)
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()
        self.driver.find_element(By.ID, "submitBTN").click()
        sleep(6)
