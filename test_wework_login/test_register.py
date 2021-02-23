# coding:  utf-8
# @Author  : LianXinPeng
# @Time    : 2021/2/23 23:42
from test_wework_login.index import Index


class TestRegister():
    def setup(self):
        self.index = Index()

    def test_register(self):
        result = self.index.goto_register().register()
        assert result
