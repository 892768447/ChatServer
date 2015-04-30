#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-4-25
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: url路由
'''
from handler.auth import AuthLoginHandler, AuthLogoutHandler, \
    AuthRegisterHandler
from handler.delete import DeleteHandler
from handler.details import GetDetailsHandler
from handler.friends import GetFriendsHandler
from handler.index import IndexHandler
from handler.socket import SocketHandler
from handler.test import TestHandler
from handler.xsrf import XsrfHandler
from handler.error import ErrorHandler


__Author__ = "By: ヽoo悾絔℅o。\nQQ: 892768447\nEmail: 892768447@qq.com\nWeb: http://wsq.qq.com/reflow/264315676"
__Copyright__ = "Copyright (c) 2015 ヽoo悾絔℅o。"
__Version__ = "Version 1.0"

urls = [ \
    (r"/xsrf", XsrfHandler), \
    (r"/login", AuthLoginHandler), \
    (r"/logout", AuthLogoutHandler), \
    (r"/reg", AuthRegisterHandler), \
    (r"/friends", GetFriendsHandler), \
    (r"/details", GetDetailsHandler), \
    (r"/delete", DeleteHandler), \
    (r"/socket", SocketHandler), \
    (r"/error", ErrorHandler), \
    (r"/test", TestHandler), \
    (r"/(.*?)", IndexHandler), \
]