#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-4-27
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: 获取好友、添加好友、删除好友
'''
from DbServer.handler.base import BaseHandler

__Author__ = "By: ヽoo悾絔℅o。\nQQ: 892768447\nEmail: 892768447@qq.com\nWeb: http://wsq.qq.com/reflow/264315676"
__Copyright__ = "Copyright (c) 2015 ヽoo悾絔℅o。"
__Version__ = "Version 1.0"

class GetFriendsHandler(BaseHandler):

    def get(self, *args, **kwargs):
        uid = int(self.get_argument("uid", 0))
        page = int(self.get_argument("page", 0))

    def post(self, *args, **kwargs):
        self.get(*args, **kwargs)
