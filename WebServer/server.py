#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-4-25
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: 
'''
import os
import sqlite3

from skylark import Database
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

from application import ChatApplication


__Author__ = "By: ヽoo悾絔℅o。\nQQ: 892768447\nEmail: 892768447@qq.com\nWeb: http://wsq.qq.com/reflow/264315676"
__Copyright__ = "Copyright (c) 2015 ヽoo悾絔℅o。"
__Version__ = "Version 1.0"

def initdb(path = None):
    Database.set_dbapi(sqlite3)
    Database.set_autocommit(True)
    Database.config(db = path if path else os.path.abspath("data/data.db"))

def start():
    initdb()
    app = ChatApplication()
    server = HTTPServer(app)
    server.listen(8000)
    IOLoop.instance().start()

def stop():
    IOLoop.instance().stop()

if __name__ == "__main__":
    start()
