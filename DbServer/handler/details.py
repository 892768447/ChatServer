#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-4-27
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: 
'''
from DbServer.handler.base import BaseHandler
from DbServer.model.relation import Relation
from DbServer.model.user import User
from lib.result import Result
from lib.status import Code_Ok, MSG


__Author__ = "By: ヽoo悾絔℅o。\nQQ: 892768447\nEmail: 892768447@qq.com\nWeb: http://wsq.qq.com/reflow/264315676"
__Copyright__ = "Copyright (c) 2015 ヽoo悾絔℅o。"
__Version__ = "Version 1.0"

class GetDetailsHandler(BaseHandler):

    def get(self, *args, **kwargs):
        uid = int(self.get_argument("uid", 0))
        fid = int(self.get_argument("fid", 0))
        name = self.get_argument("name", None)
        if name:
            # 根据用户名查找id和头像
            self._show_details_normal(User.where(User.username == name).select())
            return
        relation = Relation(uid = uid, fid = fid)
        if not relation:
            # 非好友只能查看用户名和头像
            self._show_details_normal(User.at(fid).select())
            return
        else:    # 显示所有
            self._show_details_full(User.at(fid).select())

    def post(self, *args, **kwargs):
        self.get(*args, **kwargs)

    def _show_details_normal(self, user):
        '''只显示id,头像,用户名'''
        self.finish(Result() \
            .status(Code_Ok) \
            .msg(MSG.get(Code_Ok, "")) \
            .data(dict(\
                uid = user.id, \
                name = user.username, \
                head = user.userhead, \
            )), \
        1)

    def _show_details_full(self, user):
        '''用户信息'''
        self.finish(Result() \
            .status(Code_Ok) \
            .msg(MSG.get(Code_Ok, "")) \
            .data(dict(\
                uid = user.id, \
                name = user.username, \
                head = user.userhead, \
            )), \
        1)
