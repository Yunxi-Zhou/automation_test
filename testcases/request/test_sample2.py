# 2. get the interface of the tag
# Interface association (接口关联): refers to the process of linking or connecting multiple APIs
import requests as req
import jsonpath as jp

class TestApi:
    def test_get_token(self):
        url = 'https://api.weixin.qq.com/cgi-bin/token'
        datas = {
            "grant_type": "client_credential",
            "appid": "wx74a8627810cfa308",
            "secret": "e40a02f9d79a8097df497e6aaf93ab80"
        }

        res = req.get(url, params=datas)
        print(res.json())

    def test_select_flag(self):
        url = "http://api.weixin.qq.com/cgi-bin/tags/get"
        datas = {
            "access_token": ""
        }