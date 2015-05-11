#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-4-25
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: 登录退出
'''

from tornado import web, gen
from tornado.escape import json_encode
from tornado.log import app_log

from src.handler.base import BaseHandler
from src.lib.model.relation import Relation
from src.lib.model.user import User
from src.lib.status import Code_RegNoUserName, Code_RegNoPassword, \
    Code_LoginSuccess, Code_LoginFailed, Code_UserExist, Code_RegSuccess, \
    Code_RegFailed, Code_LoginNoUsername, Code_LoginNoPassword


__Author__ = "By: ヽoo悾絔℅o。\nQQ: 892768447\nEmail: 892768447@qq.com\nWeb: http://wsq.qq.com/reflow/264315676"
__Copyright__ = "Copyright (c) 2015 ヽoo悾絔℅o。"
__Version__ = "Version 1.0"

class AuthLoginHandler(BaseHandler):

    def get(self, *args, **kwargs):
        self.render("login.html")

    @web.asynchronous
    @gen.coroutine
    def post(self, *args, **kwargs):
        username = self.get_argument("username", None)
        password = self.get_argument("password", None)
        if not username:
            self.finish(self._result(Code_LoginNoUsername), 1)
            return
        if not password:
            self.finish(self._result(Code_LoginNoPassword), 1)
            return
        result = yield gen.Task(self.task, username, password)
        self.finish(result, 1)

    @gen.coroutine
    def task(self, username, password):
        user = self.get_current_user()    # 如果用户已经登录了
        if user:
            return self._result(Code_LoginSuccess).data(user)
        # 从数据库中查询该用户
        user = User.findone(uname = username, upass = password)
        if user:
            # 登录成功
            count = Relation.where(Relation.uid == user.id).count()
            user.data.pop("upass")    # 去除密码
            user.data["count"] = count
            self.set_secure_cookie("user", json_encode(user.data), expires_days = None)    # 浏览器关闭时清除cookie
            return self._result(Code_LoginSuccess).data(user.data)
        return self._result(Code_LoginFailed)

class AuthLogoutHandler(BaseHandler):

    def get(self, *args, **kwargs):
        self.clear_cookie("user")
        self.finish(self.ok, 1)

class AuthRegisterHandler(BaseHandler):

    def get(self, *args, **kwargs):
        self.render("reg.html")

    @web.asynchronous
    @gen.coroutine
    def post(self, *args, **kwargs):
        username = self.get_argument("username", None)
        password = self.get_argument("password", None)
        if not username:
            self.finish(self._result(Code_RegNoUserName), 1)
            return
        if not password:
            self.finish(self._result(Code_RegNoPassword), 1)
            return
        result = yield gen.Task(self.task, username, password)
        self.finish(result, 1)

    @gen.coroutine
    def task(self, username, password):
        if User(uname = username) in User:
            return self._result(Code_UserExist)    # 该用户已经注册
        try:
            if User.create(uname = username, upass = password):
                return self._result(Code_RegSuccess)    # 注册成功
            return self._result(Code_RegFailed)    # 注册失败
        except Exception as err:
            app_log.error(err, exc_info = 1)
            return self.error