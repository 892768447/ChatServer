#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-4-25
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: 
'''

from tornado.web import RequestHandler

from src.lib.result import Result
from src.lib.status import Code_Error, MSG, Code_Ok, Code_TokenError
from tornado.escape import json_decode
import functools


__Author__ = "By: ヽoo悾絔℅o。\nQQ: 892768447\nEmail: 892768447@qq.com\nWeb: http://wsq.qq.com/reflow/264315676"
__Copyright__ = "Copyright (c) 2015 ヽoo悾絔℅o。"
__Version__ = "Version 1.0"

def authenticated(method):
    '''为所有方法增加登录验证'''
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        if not self.current_user:
            self.finish(Result().status(Code_Error).msg(MSG.get(Code_Error, "请先登录")))
            return
        return method(self, *args, **kwargs)
    return wrapper

class BaseHandler(RequestHandler):

    ERROR = Result().status(Code_Error).msg(MSG.get(Code_Error, "未知错误"))
    OK = Result().status(Code_Ok).msg(MSG.get(Code_Ok, ""))
    TERROR = Result().status(Code_TokenError).msg(MSG.get(Code_TokenError, "token有误"))

    @property
    def users(self):
        return self.application.users

    @property
    def terror(self):
        return self.TERROR

    @property
    def error(self):
        return self.ERROR

    @property
    def ok(self):
        return self.OK

    def _result(self, code, msg = ""):
        return Result() \
            .status(code) \
            .msg(MSG.get(code, msg))

    def get_current_user(self):
        user = self.get_secure_cookie("user")
        if not user:
            return None
        return json_decode(user)

    def finish(self, chunk = None, json = 0):
        self.set_header("Server", "Chat Server")
        if json:
            self.set_header("Content-Type", "application/json; charset=UTF-8")
        super(BaseHandler, self).finish(chunk)
