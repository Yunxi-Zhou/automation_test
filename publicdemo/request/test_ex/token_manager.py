# Manages token retrieval and storage
import requests as req
import jsonpath as jp

class TokenManager:
    def __init__(self, appid, secret, gt):
        self.appid = appid
        self.secret = secret
        self.gt = gt
        self.url = "https://api.weixin.qq.com/cgi-bin"
    
    def get_access_token(self):
        url = self.url+"/token"
        data = {
            "grant_type": self.gt,
            "appid": self.appid,
            "secret":self.secret
        }
        
        res = req.get(url, params=data)
        result = res.json()
        value = jp.jsonpath(result, "$.access_token")
        if not value:
            raise ValueError("Failed to get access token")
        return value[0]
        