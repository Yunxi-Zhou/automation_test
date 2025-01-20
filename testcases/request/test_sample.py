import random
import requests as req
import jsonpath as jp
import json
import re
class TestApi:
    access_token = ""
    csrf_token = ""
    sess = req.session()
    # 1. get the authentication code access token interface
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

    # 2. get the interface of the tag 获取已创建的标签接口
    # Interface association (接口关联): refers to the process of linking or connecting multiple APIs
    '''
    rule of jsonpath expression:
    $ root node
    . child node (sub-node) -> $.access_token
    .. recursion achieve child node
    [] represent get the value of list, start at 0 -> [{id:0}, {id:1}, {id:2}]
    '''
    def test_select_flag(self):
        url = "https://api.weixin.qq.com/cgi-bin/tags/get"
        datas = {
            "access_token": TestApi.access_token
        }
        res = req.get(url, params=datas)
        print(res.json())

    # 3. create the interface of the tag
    def test_create_flag(self):
        url = "https://api.weixin.qq.com/cgi-bin/tags/create?access_token="+TestApi.access_token
        datas = {"tag":{"name":"广东"+str(random.randint(10000,99999))}}
        res = req.post(url, json=datas)
        # print(res.json())
        rs = json.loads(json.dumps(res.json()).replace("\\\\","\\"))
        print(rs)
    
    # 4. delete file
    def test_file_upload(self):
        url = "https://api.weixin.qq.com/cgi-bin/media/upload?acpi.access_token"
        data = {"media":open("/Users/ethan/Downloads/IMG_0184.jpg","rb")}
        res = req.post(url, files=data)
        print(res.json())
        
    # cookie association interface
    def test_start(self):
        url = "http://47.107.116.139/phpwind/"
        res = TestApi.sess.request(method="get",url=url)
        result = res.text  # string
        # print(result)
        TestApi.csrf_token = re.search('name="csrf_token" value="(.*?)"',result).group(1)
        print(TestApi.csrf_token)
        
    def test_login(self):
        url = "http://47.107.116.139/phpwind/index.php?m=u&c=login&a=dorun"
        data = {
            "username":"zhouy218",
            "password":"136671",
            "csrf_token":TestApi.csrf_token,
            "back_url":"http://47.107.116.139/phpwind/",
            "invite":""
        }
        headers = {
            "Accept":"application/json, text/javascript, /; q=0.01",
            "X-Requested-With":"XMLHttpRequest"
        }
        res = TestApi.sess.request(method="post", url=url, data=data, headers=headers)
        print(res.json())

if __name__ == '__main__':
    test = TestApi()
    # test.test_get_token()
    # test.test_select_flag()
    # test.test_create_flag()
    # test.test_file_upload()
    test.test_start()
    test.test_login()