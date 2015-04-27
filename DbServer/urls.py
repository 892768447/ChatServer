#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-4-25
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: url路由
'''
from DbServer.handler.auth import AuthLoginHandler, AuthRegisterHandler
from DbServer.handler.delete import DeleteHandler
from DbServer.handler.details import GetDetailsHandler
from DbServer.handler.friends import GetFriendsHandler
from DbServer.handler.index import IndexHandler


__Author__ = "By: ヽoo悾絔℅o。\nQQ: 892768447\nEmail: 892768447@qq.com\nWeb: http://wsq.qq.com/reflow/264315676"
__Copyright__ = "Copyright (c) 2015 ヽoo悾絔℅o。"
__Version__ = "Version 1.0"

urls = [ \
    (r"/login", AuthLoginHandler), \
    (r"/reg", AuthRegisterHandler), \
    (r"/friends", GetFriendsHandler), \
    (r"/details", GetDetailsHandler), \
    (r"/delete", DeleteHandler), \
    (r"/(.*?)", IndexHandler), \
]
