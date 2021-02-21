# coding:  utf-8
# @Author  : LianXinPeng
# @Time    : 2021/2/21 14:22
from selenium.webdriver.common.by import By

from Base import Base

"""
frame存在两种，一种是嵌套的；一种是未嵌套的
切换frame
switch_to.frame()   根据元素id或者index切换
switch_to.default_content()   切换到默认frame
switch_to.parent_frame()      切换到父级frame

未嵌套的frame
switch_to_frame("frame的id")
switch_to_frame("frame-index")  frame无ID的时候根据索引来处理，索引从0开始

嵌套的frame
对于嵌套的先进入到iframe的父节点，再进到子节点；然后可以对子节点里面的对象进行处理和操作
switch_to.frame("父节点")
switch_to.frame("子节点")
"""


class TestFrame(Base):
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        print(self.driver.find_element(By.ID, "draggable").text)

        # self.driver.switch_to.parent_frame()   # 切换到父级frame
        self.driver.switch_to.default_content()  # 切换到默认frame
        print(self.driver.find_element(By.ID, "submitBTN").text)
