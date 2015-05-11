#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-4-25
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: 获取好友、添加好友、删除好友、查看好友资料
'''

from tornado import web, gen
from tornado.log import app_log

from src.handler.base import BaseHandler, authenticated
from src.lib.model.friends import Friends
from src.lib.result import Result
from src.lib.status import MSG, Code_Ok


__Author__ = "By: ヽoo悾絔℅o。\nQQ: 892768447\nEmail: 892768447@qq.com\nWeb: http://wsq.qq.com/reflow/264315676"
__Copyright__ = "Copyright (c) 2015 ヽoo悾絔℅o。"
__Version__ = "Version 1.0"

class GetFriendsHandler(BaseHandler):

    def get(self, *args, **kwargs):
        self.render("friends.html")

    @authenticated
    @web.asynchronous
    @gen.coroutine
    def post(self, *args, **kwargs):
        uid = self.get_argument("uid", 0)
        page = self.get_argument("page", 0)
        result = yield gen.Task(self.task, uid, page)
        self.finish(result, 1)

    @gen.coroutine
    def task(self, uid, page):
        try:
            uid = int(uid)
            page = int(page)
        except Exception as err:
            app_log.error(err, exc_info = 1)
            return self.error
        try:
            # 分页查询
            friends = Friends.at(uid).limit(page * 10 + 10, page * 10).select()
            return Result() \
                .status(Code_Ok) \
                .msg(MSG.get(Code_Ok, "")) \
                .data([friend.data for friend in friends])
        except Exception as err:
            app_log.error(err, exc_info = 1)
        return self.error
