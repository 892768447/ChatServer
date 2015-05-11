#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-4-25
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: url路由
'''
from src.handler.auth import AuthLoginHandler, AuthLogoutHandler, \
    AuthRegisterHandler
from src.handler.delete import DeleteHandler
from src.handler.details import GetDetailsHandler
from src.handler.error import ErrorHandler
from src.handler.friends import GetFriendsHandler
from src.handler.groups import GetGroupsHandler, AddGroupsHandler, \
    DelGroupsHandler, ModifyGroupsHandler
from src.handler.index import IndexHandler
from src.handler.socket import SocketHandler
from src.handler.test import TestHandler
from src.handler.xsrf import XsrfHandler


__Author__ = "By: ヽoo悾絔℅o。\nQQ: 892768447\nEmail: 892768447@qq.com\nWeb: http://wsq.qq.com/reflow/264315676"
__Copyright__ = "Copyright (c) 2015 ヽoo悾絔℅o。"
__Version__ = "Version 1.0"

urls = [ \
    (r"/xsrf", XsrfHandler), \
    (r"/login", AuthLoginHandler), \
    (r"/logout", AuthLogoutHandler), \
    (r"/reg", AuthRegisterHandler), \
    (r"/friends", GetFriendsHandler), \
    (r"/groups/add", AddGroupsHandler), \
    (r"/groups/del", DelGroupsHandler), \
    (r"/groups/modify", ModifyGroupsHandler), \
    (r"/groups", GetGroupsHandler), \
    (r"/details", GetDetailsHandler), \
    (r"/delete", DeleteHandler), \
    (r"/socket", SocketHandler), \
    (r"/error", ErrorHandler), \
    (r"/test", TestHandler), \
    (r"/(.*?)", IndexHandler), \
]
