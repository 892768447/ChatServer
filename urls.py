#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-4-25
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: url路由
'''
from handler.auth import AuthLoginHandler, AuthLogoutHandler
from handler.friends import GetFriendsHandler
from handler.index import IndexHandler
from handler.xsrf import XsrfHandler


__Author__ = "By: ヽoo悾絔℅o。\nQQ: 892768447\nEmail: 892768447@qq.com\nWeb: http://wsq.qq.com/reflow/264315676"
__Copyright__ = "Copyright (c) 2015 ヽoo悾絔℅o。"
__Version__ = "Version 1.0"

urls = [ \
    (r"/xsrf", XsrfHandler), \
    (r"/login", AuthLoginHandler), \
    (r"/logout", AuthLogoutHandler), \
    (r"/friends", GetFriendsHandler), \
    (r"/(.*?)", IndexHandler), \
]