#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-4-27
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: 
'''
from tornado import web, gen
from tornado.log import app_log

from handler.base import BaseHandler, authenticated
from lib.model.relation import Relation
from lib.model.user import User
from lib.result import Result
from lib.status import Code_Ok, MSG


__Author__ = "By: ヽoo悾絔℅o。\nQQ: 892768447\nEmail: 892768447@qq.com\nWeb: http://wsq.qq.com/reflow/264315676"
__Copyright__ = "Copyright (c) 2015 ヽoo悾絔℅o。"
__Version__ = "Version 1.0"

class GetDetailsHandler(BaseHandler):

    def get(self, *args, **kwargs):
        self.render("details.html")

    @authenticated
    @web.asynchronous
    @gen.coroutine
    def post(self, *args, **kwargs):
        uid = self.get_argument("uid", 0)
        fid = self.get_argument("fid", 0)
        name = self.get_argument("name", None)
        result = yield gen.Task(self.task, uid, fid, name)
        self.finish(result, 1)

    @gen.coroutine
    def task(self, uid, fid, name):
        try:
            if name:
                # 根据用户名查找id和头像
                return self._show_details_normal(User.findone(User.username == name))
            if Relation(uid = uid, fid = fid) not in Relation:
                # 非好友只能查看用户名和头像
                return self._show_details_normal(User.findone(User.id == fid))    # @UndefinedVariable
            else:    # 显示所有
                return self._show_details_full(User.findone(User.id == fid))    # @UndefinedVariable
        except Exception as err:
            app_log.error(err, exc_info = 1)
        return self.error

    def _show_details_normal(self, user):
        '''只显示id,头像,用户名'''
        if user is None:
            return self.error
        return Result() \
            .status(Code_Ok) \
            .msg(MSG.get(Code_Ok, "")) \
            .data(dict(\
                uid = user.id, \
                name = user.username, \
                head = user.userhead, \
            ))

    def _show_details_full(self, user):
        '''用户信息'''
        return Result() \
            .status(Code_Ok) \
            .msg(MSG.get(Code_Ok, "")) \
            .data(dict(\
                uid = user.id, \
                name = user.username, \
                head = user.userhead, \
                time = user.regtime, \
            ))
