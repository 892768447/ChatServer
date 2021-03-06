#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-4-29
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: 
'''
import time

from tornado import gen

from src.handler.base import BaseHandler


__Author__ = "By: ヽoo悾絔℅o。\nQQ: 892768447\nEmail: 892768447@qq.com\nWeb: http://wsq.qq.com/reflow/264315676"
__Copyright__ = "Copyright (c) 2015 ヽoo悾絔℅o。"
__Version__ = "Version 1.0"

class TestHandler(BaseHandler):

    def test(self, num):
        print("num: ", num)
        time.sleep(num)
        return num

    @gen.coroutine
    def get(self, *args, **kwargs):
        num = self.get_argument("num", 1)
        result = yield gen.Task(self.test, int(num))
        self.finish("time: " + str(result))
