from commons.request_util import RequestUtil
from commons.yaml_util import write_yaml, read_yaml
import re
import pytest
class TestPhpWind:
    # cookie association interface
    @pytest.mark.smoke
    def test_start(self):
        url = "http://47.107.116.139/phpwind/"
        res = RequestUtil().all_send_request(method="get",url=url)
        result = res.text  # string
        datas = {"csrf_token":re.search('name="csrf_token" value="(.*?)"',result).group(1)}
        write_yaml(datas)
        # print(result)
        # TestPhpWind.csrf_token = 
        # print(TestPhpWind.csrf_token) 
        
    def test_login(self):
        # print(sql)
        url = "http://47.107.116.139/phpwind/index.php?m=u&c=login&a=dorun"
        data = {
            "username":"zhouy218",
            "password":"136671",
            "csrf_token":read_yaml("csrf_token"),
            "back_url":"http://47.107.116.139/phpwind/",
            "invite":""
        }
        headers = {
            "Accept":"application/json, text/javascript, /; q=0.01",
            "X-Requested-With":"XMLHttpRequest"
        }
        RequestUtil().all_send_request(method="post", url=url, data=data, headers=headers)
    
if __name__ == '__main__':
    TestPhpWind().test_start()
    TestPhpWind().test_login()