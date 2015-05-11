#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-4-29
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: 
'''
from urllib.parse import urlencode

from tornado.httpclient import HTTPRequest, HTTPClient


__Author__ = "By: ヽoo悾絔℅o。\nQQ: 892768447\nEmail: 892768447@qq.com\nWeb: http://wsq.qq.com/reflow/264315676"
__Copyright__ = "Copyright (c) 2015 ヽoo悾絔℅o。"
__Version__ = "Version 1.0"

# Set-Cookie


client = HTTPClient()

url = "http://localhost:8000/login"
method = "POST"
headers = None
body = urlencode({"username":"admin", "password":"admin"})

request = HTTPRequest(url = url, method = method, headers = headers, body = body)
result = client.fetch(request)
print(result)
cookies = result.headers.get_list("set-cookie")
print(cookies)
print(result.body)

print(".....................")

url = "http://localhost:8000/friends"
method = "POST"
headers = {"Cookie":cookies[0]}
body = urlencode({"uid":1, "page":0})

request = HTTPRequest(url = url, method = method, headers = headers, body = body)
result = client.fetch(request)
print(result)
print(result.headers.get_list("set-cookie"))
print(result.body)

