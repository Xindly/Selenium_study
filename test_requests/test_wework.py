# coding:  utf-8
# @Author  : LianXinPeng
# @Time    : 2021/3/15 21:45
import pytest
import requests


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

    def test_create(self, token, userid, mobile, name="五月天", department=None):
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

    def test_edit_user(self, token, userid, mobile="13700000001", name="六月的雨"):
        """
        请求方式：POST（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=ACCESS_TOKEN
        :return:
        """
        request_body = {
            "userid": userid,
            "name": name,
            "mobile": mobile
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
        print(user.json())

    def test_wework(self, token):
        """
        整体测试
        :return:
        """
        self.test_create(token, "wuyuetian", "13799999991")
        self.test_get_user(token, "wuyuetian")
