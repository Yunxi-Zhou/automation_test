# Handles API requests and response

import requests as req
import json

class APIHandler():
    def __init__(self,access_token):
        self.access_token = access_token
        self.url = "https://api.weixin.qq.com/cgi-bin"

    def get_tags(self):
        url = self.url+"/tags/get"
        params = {"access_token": self.access_token}
        res = req.get(url, params=params)
        return res.json()

    def create_tag(self, name):
        url = self.url+"/tags/create?access_token={self.access_token}"
        data = {"tag":{"name":name}}
        res = req.post(url, json=data)
        return res.json()