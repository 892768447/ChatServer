#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-4-29
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: 
'''
import time

from handler.base import BaseHandler


try:
    from tornado.curl_httpclient import CurlAsyncHTTPClient as AsyncClient    # @UnusedImport
except:
    from tornado.httpclient import AsyncHTTPClient as AsyncClient    # @UnusedImport @Reimport

__Author__ = "By: ヽoo悾絔℅o。\nQQ: 892768447\nEmail: 892768447@qq.com\nWeb: http://wsq.qq.com/reflow/264315676"
__Copyright__ = "Copyright (c) 2015 ヽoo悾絔℅o。"
__Version__ = "Version 1.0"

class TestHandler(BaseHandler):

    def get(self, *args, **kwargs):
        num = self.get_argument("num", None)
        if num is None:
            self.finish("num is none")
            return
        try:
            num = int(num)
        except:
            num = 1
        time.sleep(num)
        self.finish(dict(time = num), 1)
