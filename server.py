#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-4-25
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: 
'''
from application import ChatApplication
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

__Author__ = "By: ヽoo悾絔℅o。\nQQ: 892768447\nEmail: 892768447@qq.com\nWeb: http://wsq.qq.com/reflow/264315676"
__Copyright__ = "Copyright (c) 2015 ヽoo悾絔℅o。"
__Version__ = "Version 1.0"

def start():
    app = ChatApplication()
    server = HTTPServer(app)
    server.listen(8000)
    IOLoop.instance().start()

def stop():
    IOLoop.instance().stop()

if __name__ == "__main__":
    start()