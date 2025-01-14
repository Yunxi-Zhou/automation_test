# part 2 of automation test
# receive response

import requests as req
from certifi import contents

res = req.get(url, params=None, **kwargs)
print(res.text)  return text information
print(res.json())  return .json
print(res.content)  return byte contents
print(res.status_code)  return status code
print(res.reason) return reason information
print(res.cookies)  return cookies
print(res.encoding)  return encoding e.g: encoding('utf-8')
print(res.headers)  return request headers
print(res.request.(requests data))  return request data



