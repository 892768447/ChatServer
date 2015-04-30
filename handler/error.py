#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-4-29
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: 
'''
from tornado.web import RequestHandler

from lib.result import Result
from lib.status import Code_Error, MSG


__Author__ = "By: ヽoo悾絔℅o。\nQQ: 892768447\nEmail: 892768447@qq.com\nWeb: http://wsq.qq.com/reflow/264315676"
__Copyright__ = "Copyright (c) 2015 ヽoo悾絔℅o。"
__Version__ = "Version 1.0"

class ErrorHandler(RequestHandler):

    def get(self, *args, **kwargs):
        self.finish(Result().status(Code_Error).msg(MSG.get(Code_Error, "未知错误")))

    def post(self, *args, **kwargs):
        self.get(*args, **kwargs)
