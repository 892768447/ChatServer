#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-4-25
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: 
'''
from tornado import gen
from tornado.web import RequestHandler, HTTPError
from handler.base import BaseHandler
from tornado.escape import json_encode


__Author__ = "By: ヽoo悾絔℅o。\nQQ: 892768447\nEmail: 892768447@qq.com\nWeb: http://wsq.qq.com/reflow/264315676"
__Copyright__ = "Copyright (c) 2015 ヽoo悾絔℅o。"
__Version__ = "Version 1.0"

class AuthLoginHandler(BaseHandler):

    @gen.coroutine
    def post(self, *args, **kwargs):
        data = self.get_argument("data", None)
        if not data:
            raise HTTPError(500, "data is none")
        # 解析登录包并判断
        # 登录成功放入cookie(时间为1天)
        self.set_secure_cookie("user", json_encode(data), 1)
        self.finish("登陆成功")

class AuthLogoutHandler(RequestHandler):

    def get(self, *args, **kwargs):
        self.clear_cookie("user")
        self.write("注销")
