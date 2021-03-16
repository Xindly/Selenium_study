# coding:  utf-8
# @Author  : LianXinPeng
# @Time    : 2021/3/15 21:45
import random
import re

import pytest
import requests


def test_create_data():
    """userid,name,mobile"""
    # data = [(str(random.randint(0, 9999999)), "五月天", str(random.randint(13800000000, 13900000000))) for x in range(6)]
    data = [("wuyue" + str(x), "五月天", "138%08d" % x) for x in range(10 )]
    return data


class TestWework():
    @pytest.fixture(scope="session")
    def token(self):
        """
        获取token
        https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ID&corpsecret=SECRET
        :return:
        """
        request_params = {
            "corpid": "ww5940ffa00466c58a",
            "corpsecret": "3CBjYpH0yBduo1fdzGaPwbqqYTmQOIAxVxFjRCbvRac"
        }
        ID = "ww5940ffa00466c58a"
        SECRET = "3CBjYpH0yBduo1fdzGaPwbqqYTmQOIAxVxFjRCbvRac"
        r = requests.get(
            "https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=request_params)
        return r.json()['access_token']

    def test_create(self, token, userid, name, mobile, department=None):
        """
        请求方式：POST（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN
        :return:
        """
        if department is None:
            department = [1]
        request_body = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        user = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}",
                             json=request_body)
        return user.json()

    def test_get_user(self, token, userid):
        """
        请求方式：GET（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=ACCESS_TOKEN&userid=USERID
        :return:
        """
        user_id = "wuyuetian"
        user = requests.get(
            f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid={userid}")
        return user.json()

    def test_edit_user(self, token, userid, name="六月的雨"):
        """
        请求方式：POST（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=ACCESS_TOKEN
        :return:
        """
        request_body = {
            "userid": userid,
            "name": name
        }
        edit_user = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}",
                                  json=request_body)
        return edit_user.json()

    def test_delete_user(self, token, userid):
        """
        请求方式：GET（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token=ACCESS_TOKEN&userid=USERID
        :return:
        """
        user_id = "wuyuetian"
        user = requests.get(
            f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid={userid}")
        return user.json()

    @pytest.mark.parametrize("user_id, name, mobile", test_create_data())
    def test_wework(self, token, user_id, name, mobile):
        """
        整体测试
        :return:
        """
        try:
            assert "created" == self.test_create(token, user_id, name, mobile)["errmsg"]
        except AssertionError as e:
            if "mobile existed" in e.__str__():
                re_userid = re.findall(":(.*)'", e.__str__())[0]
                self.test_delete_user(token, re_userid)
                assert "created" == self.test_create(token, user_id, name, mobile)["errmsg"]
        assert name == self.test_get_user(token, user_id)["name"]
        assert "updated" == self.test_edit_user(token, user_id, name="八月的风")["errmsg"]
        assert "八月的风" == self.test_get_user(token, user_id)["name"]
        assert "deleted" == self.test_delete_user(token, user_id)["errmsg"]
        assert 60111 == self.test_get_user(token, user_id)["errcode"]
