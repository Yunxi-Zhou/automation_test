# 2. get the interface of the tag 获取已创建的标签接口
# Interface association (接口关联): refers to the process of linking or connecting multiple APIs
import requests as req
import jsonpath as jp

'''
rule of jsonpath expression:
$ root node
. child node (sub-node) -> $.access_token
.. recursion achieve child node
[] represent get the value of list, start at 0 -> [{id:0}, {id:1}, {id:2}]
'''


class TestApi:
    access_token = ""
    def test_get_token(self):
        url = 'https://api.weixin.qq.com/cgi-bin/token'
        datas = {
            "grant_type": "client_credential",
            "appid": "wx74a8627810cfa308",
            "secret": "e40a02f9d79a8097df497e6aaf93ab80"
        }

        res = req.get(url, params=datas)
        result = res.json()
        print(result)

        # get access token
        value = jp.jsonpath(result, "$.access_token")
        # print(value)
        TestApi.access_token = value[0]

    def test_select_flag(self):
        url = "http://api.weixin.qq.com/cgi-bin/tags/get"
        datas = {
            "access_token": TestApi.access_token
        }
        res = req.get(url, params=datas)
        print(res.json())

if __name__ == '__main__':
    t = TestApi()
    t.test_get_token()
    t.test_select_flag()