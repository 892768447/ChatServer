#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-4-25
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: 
'''
import os
import sys
sys.path.append(os.path.split(os.path.dirname(__file__))[0])    # 把父目录添加到sys.path中

import sqlite3

from skylark import Database
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

from src import lib
from src.lib.application import ChatApplication


__Author__ = "By: ヽoo悾絔℅o。\nQQ: 892768447\nEmail: 892768447@qq.com\nWeb: http://wsq.qq.com/reflow/264315676"
__Copyright__ = "Copyright (c) 2015 ヽoo悾絔℅o。"
__Version__ = "Version 1.0"

def initdb(path = None):
    Database.set_dbapi(sqlite3)
    Database.set_autocommit(True)
    Database.config(db = path if path else lib.DBPATH, check_same_thread = False)

def start():

    lib.TEMPLATE = os.path.abspath("template")
    lib.STATIC = os.path.abspath("static")
    lib.DBPATH = os.path.abspath("data/data.db")

    initdb()    # 初始化连接数据库

    app = ChatApplication()
    server = HTTPServer(app)
    server.listen(8000)
    IOLoop.instance().start()

def stop():
    IOLoop.instance().stop()

if __name__ == "__main__":
    start()
