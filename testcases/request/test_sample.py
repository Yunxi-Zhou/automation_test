# 3. create the interface of the tag

import random
import requests as req
import jsonpath as jp
import json

class TestApi:
    access_token = ""

    def test_get_token(self):
        # ?grant_type=client_credential&appid=appid&secret=secret
        # grant type 用户类型
        # appid 第三方用户唯一id
        # secret 第三方用户唯一密钥
        url = "https://api.weixin.qq.com/cgi-bin/token"
        datas = {
            "grant_type": "client_credential",
            "appid": "wx74a8627810cfa308",
            "secret": "e40a02f9d79a8097df497e6aaf93ab80"
        }

        res = req.get(url, params=datas)
        # return .json -> .json: data consist of {} and []
        # print(res.text)
        result = res.json()
        print(result)

        # get access token
        value = jp.jsonpath(result, "$.access_token")
        # print(value)
        TestApi.access_token = value[0]

    def test_select_flag(self):
        url = "https://api.weixin.qq.com/cgi-bin/tags/get"
        datas = {
            "access_token": TestApi.access_token
        }
        res = req.get(url, params=datas)
        print(res.json())

    def test_create_flag(self):
        url = "https://api.weixin.qq.com/cgi-bin/tags/create?access_token="+TestApi.access_token
        datas = {"tag":{"name":"广东"+str(random.randint(10000,99999))}}
        res = req.post(url, json=datas)
        # print(res.json())
        rs = json.loads(json.dumps(res.json()).replace("\\\\","\\"))
        print(rs)

if __name__ == '__main__':
    test = TestApi()
    test.test_get_token()
    test.test_select_flag()
    test.test_create_flag()