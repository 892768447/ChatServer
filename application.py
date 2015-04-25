#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-4-25
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: 这个文件的核心任务是完成 tornado.web.Application() 的实例化
'''
from tornado.web import Application
from urls import urls

__Author__ = "By: ヽoo悾絔℅o。\nQQ: 892768447\nEmail: 892768447@qq.com\nWeb: http://wsq.qq.com/reflow/264315676"
__Copyright__ = "Copyright (c) 2015 ヽoo悾絔℅o。"
__Version__ = "Version 1.0"

class ChatApplication(Application):
    '''Chat Application'''

    def __init__(self):
        settings = { \
            "cookie_secret" : "", \
            "xsrf_cookies" : "", \
            "template_path" : "", \
            "static_path" : "", \
            "debug" : False \
        }
        super(ChatApplication, self).__init__(urls, **settings)
