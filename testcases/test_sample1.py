# 1. get the authentication code access token interface
import requests as req

class TestApi:
    def test_get_token(self):
        # ?grant_type=client_credential&appid=appid&secret=secret
        # grant type 用户类型
        # appid 第三方用户唯一id
        # secret 第三方用户唯一密钥
        url = 'https://api.weixin.qq.com/cgi-bin/token'
        datas = {
            "grant_type": "client_credential",
            "appid": "wx74a8627810cfa308",
            "secret": "e40a02f9d79a8097df497e6aaf93ab80"
        }

        res = req.get(url, params=datas)
        # return .json -> .json: data consist of {} and []
        # print(res.text)
        print(res.json())

if __name__ == '__main__':
    test = TestApi()
    test.test_get_token()

