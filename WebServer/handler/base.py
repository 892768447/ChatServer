#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-4-25
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: 
'''

from tornado.web import RequestHandler


__Author__ = "By: ヽoo悾絔℅o。\nQQ: 892768447\nEmail: 892768447@qq.com\nWeb: http://wsq.qq.com/reflow/264315676"
__Copyright__ = "Copyright (c) 2015 ヽoo悾絔℅o。"
__Version__ = "Version 1.0"

class BaseHandler(RequestHandler):

    @property
    def tokens(self):
        return self.application.tokens

    def finish(self, chunk = None, json = 0):
        self.set_header("Server", "Chat Server")
        if json:
            self.set_header("Content-Type", "application/json; charset=UTF-8")
        super(BaseHandler, self).finish(chunk)
