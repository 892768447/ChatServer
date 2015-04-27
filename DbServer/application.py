#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-4-25
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: 这个文件的核心任务是完成 tornado.web.Application() 的实例化
'''
from tornado.web import Application
from DbServer.urls import urls

__Author__ = "By: ヽoo悾絔℅o。\nQQ: 892768447\nEmail: 892768447@qq.com\nWeb: http://wsq.qq.com/reflow/264315676"
__Copyright__ = "Copyright (c) 2015 ヽoo悾絔℅o。"
__Version__ = "Version 1.0"

class DbApplication(Application):
    '''Chat Application'''

    def __init__(self):
        settings = { \
            "cookie_secret" : "DbServer", \
            "debug" : False \
        }
        super(DbApplication, self).__init__(urls, **settings)