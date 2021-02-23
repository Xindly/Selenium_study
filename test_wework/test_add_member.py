# coding:  utf-8
# @Author  : LianXinPeng
# @Time    : 2021/2/24 0:09
from test_wework.index import Index


class TestAddmember():
    def setup(self):
        self.index = Index()

    def test_add_member(self):
        self.index.goto_add_member().add_member()
