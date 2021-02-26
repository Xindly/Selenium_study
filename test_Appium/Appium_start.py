# coding:  utf-8
# @Author  : LianXinPeng
# @Time    : 2021/2/26 15:43
from time import sleep

from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = '127.0.0.1:7555'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = 'com.android.settings.Settings'

# 是否再测试前后重置相关环境（比如首次打开弹框，或者是登录信息）
"""
unicodeKeyBoard
是否需要输入非英文之外的语言
resetKeyBoard
重置输入法

提升运行速度 
dontStopAppOnReset
首次启动的时候，不停止app
skipDeviceInitialization
跳过安装、权限设置等
"""
desired_caps['noReset'] = True

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

sleep(10)
driver.quit()
