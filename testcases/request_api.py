import requests as req

req.get(url, params=None, **kwargs)
# url: URL for the new :class:`Request` object.
# params: (optional) Dictionary, list of tuples or bytes to send in the query string for the :class:`Request`.
# \*\*kwargs: Optional arguments that ``request`` takes.
req.post(url, data=None, json=None, **kwargs)
# url – URL for the new :class:`Request` object.
# data – (optional) Dictionary, list of tuples, bytes, or file-like object to send in the body of the :class:`Request`.
# json – (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
req.put(url, data=None, **kwargs)
# url – URL for the new :class:`Request` object.
# data – (optional) Dictionary, list of tuples, bytes, or file-like object to send in the body of the :class:`Request`.
req.delete(url, **kwargs)
# url – URL for the new :class:`Request` object.

# The above method internally calls the `request` method

req.request(method, url, **kwargs)
# method – method for the new :class:`Request` object: GET, OPTIONS, HEAD, POST, PUT, PATCH, or DELETE.
# url – URL for the new :class:`Request` object.

# `request` method calls the method below (Automatically associating interfaces with cookie associations)
session.request(method=method, url=url, **kwargs)
'''
method,  call for method方式
url,  call for url路径
params=None,  get() call for parameters
data=None,  post(),put() call for parameters
json = None, post() call for parameters
headers=None,  call for headers
cookies=None,  cookies  # cookie: 存储用户会话信息，比如登陆状态，用户标识
files=None,  upload files
-----------------------------------
auth=None,  authentication #authentication: 鉴权，验证用户身份的过程， 确保请求者是其声称的身份
timeout=None,  timeout handling
allow_redirects=True,  whether redirects or not (是否重定向)
proxies=None,  whether set proxies or not (是否设置代理)
hooks=None,  hooks function
stream=None, file download
verify=None,  certification vertify (证书验证)
cert=None,  CA certification
'''

'''
Ex.1 req.get()
step 1: req.get(url, params=None, **kwargs)
step 2: req.request(method=GET, url_r=url, **kwargs=(params=None))
step 3: session.request(method=GET, url_s=url_r, **kwargs=(params=None))
'''

'''
Ex.2 req.post()
step 1: req.post(url, data=None, json=None, **kwargs)
step 2: req.request(method=POST, url_r=url, **kwargs=(data=None, json=None))
step 3: session.request(method=POST, url_s=url_r, **kwargs=(data=None, json=None))
'''

# generate a session object
req.session()
