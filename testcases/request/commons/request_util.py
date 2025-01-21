import requests

class RequestUtil:
    sess = requests.session()
    
    # common send requests
    def all_send_request(self, **kwargs):
       res = RequestUtil.sess.request(**kwargs)
       print("method: "+kwargs["method"])
       print(res.text)
       return res