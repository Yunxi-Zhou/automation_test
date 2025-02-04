import requests

class RequestUtil:
   sess = requests.session()
    
   # common send requests
   # 原理： 请求头： keep-alive
   # Connection: keep-alive 保持活跃
   def all_send_request(self, **kwargs):
      res = RequestUtil.sess.request(**kwargs)
   #    print("method: "+kwargs["method"])
   #    print(res.text)
      return res