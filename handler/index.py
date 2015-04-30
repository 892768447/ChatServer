#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-4-25
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: 首页
'''

from handler.base import BaseHandler


__Author__ = "By: ヽoo悾絔℅o。\nQQ: 892768447\nEmail: 892768447@qq.com\nWeb: http://wsq.qq.com/reflow/264315676"
__Copyright__ = "Copyright (c) 2015 ヽoo悾絔℅o。"
__Version__ = "Version 1.0"

class IndexHandler(BaseHandler):

    def get(self, *args, **kwargs):
        self.render("index.html", count = len(self.users))

    def post(self, *args, **kwargs):
        self.render("index.html", count = len(self.users))