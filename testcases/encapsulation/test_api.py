import random
import jsonpath as jp
import json
import pytest
from commons.request_util import RequestUtil


class TestApi:
    access_token = ""
    
    # def setup_class(self):
    #     print("before functions request: connect database")
            
    # def teardown_class(self):
    #     print("after function request: close database")
    
    # 1. get the authentication code access token interface
    @pytest.mark.smoke
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

        res = RequestUtil().all_send_request(method="get",url=url, params=datas)
        # return .json -> .json: data consist of {} and []
        # print(res.text)
        result = res.json()
        # print(result)

        # get access token
        value = jp.jsonpath(result, "$.access_token")
        # print(value)
        TestApi.access_token = value[0]

    # 2. get the interface of the tag 获取已创建的标签接口
    # Interface association (接口关联): refers to the process of linking or connecting multiple APIs
    '''
    rule of jsonpath expression:
    $ root node
    . child node (sub-node) -> $.access_token
    .. recursion achieve child node
    [] represent get the value of list, start at 0 -> [{id:0}, {id:1}, {id:2}]
    '''
    @pytest.mark.user_manager
    def test_select_flag(self):
        url = "https://api.weixin.qq.com/cgi-bin/tags/get"
        datas = {
            "access_token": TestApi.access_token
        }
        res = RequestUtil().all_send_request(method="get", url=url, params=datas)

    # 3. create the interface of the tag
    def test_create_flag(self):
        url = "https://api.weixin.qq.com/cgi-bin/tags/create?access_token="+TestApi.access_token
        datas = {"tag":{"name":"广东"+str(random.randint(10000,99999))}}
        res = RequestUtil().all_send_request(method="post",url=url, json=datas)
        # print(res.json())
        rs = json.loads(json.dumps(res.json()).replace("\\\\","\\"))
    
    # 4. delete file
    def test_file_upload(self):
        url = "https://api.weixin.qq.com/cgi-bin/media/upload?acpi.access_token"
        data = {"media":open("/Users/ethan/Downloads/IMG_0184.jpg","rb")}
        res = RequestUtil().all_send_request(method="post", url=url, files=data)
        

if __name__ == '__main__':
    test = TestApi()
    test.test_get_token()
    test.test_select_flag()
    test.test_create_flag()
    test.test_file_upload()