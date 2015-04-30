#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-4-25
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: 登录退出
'''

from tornado import web, gen
from tornado.log import app_log

from handler.base import BaseHandler
from lib.model.relation import Relation
from lib.model.user import User
from lib.result import Result
from lib.status import Code_RegNoUserName, MSG, Code_RegNoPassword, \
    Code_LoginSuccess, Code_LoginFailed, Code_UserExist, Code_RegSuccess, \
    Code_RegFailed
from tornado.escape import json_encode

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
            self.finish(Result() \
                .status(Code_RegNoUserName) \
                .msg(MSG.get(Code_RegNoUserName, "没有填写用户名")), \
            1)
            return
        if not password:
            self.finish(Result() \
                .status(Code_RegNoPassword) \
                .msg(MSG.get(Code_RegNoPassword, "没有填写密码")), \
            1)
            return
        result = yield gen.Task(self.task, username, password)
        self.finish(result, 1)

    @gen.coroutine
    def task(self, username, password):
        user = self.get_current_user()    # 如果用户已经登录了
        if user:
            return Result() \
                .status(Code_LoginSuccess) \
                .msg(MSG.get(Code_LoginSuccess, "登录成功")) \
                .data(user)
        # 从数据库中查询该用户
        user = User.findone(username = username, password = password)
        if user:
            # 登录成功
            count = Relation.where(Relation.uid == user.id).count()
            return self._login_success(user, count)
        return self._login_failed()

    def _login_success(self, user, count):
        '''登录成功'''
        data = dict(uid = user.id, \
            name = user.username, pwd = user.password, \
            head = user.userhead, count = count)
        self.set_secure_cookie("user", json_encode(data), expires_days = None)    # 浏览器关闭时清除cookie
        return Result() \
            .status(Code_LoginSuccess) \
            .msg(MSG.get(Code_LoginSuccess, "登录成功")) \
            .data(data)

    def _login_failed(self):
        '''登录失败'''
        return Result() \
            .status(Code_LoginFailed) \
            .msg(MSG.get(Code_LoginFailed, "用户不存在或者用户名密码错误"))

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
            self.finish(Result() \
                .status(Code_RegNoUserName) \
                .msg(MSG.get(Code_RegNoUserName, "没有填写用户名")), \
            1)
            return
        if not password:
            self.finish(Result() \
                .status(Code_RegNoPassword) \
                .msg(MSG.get(Code_RegNoPassword, "没有填写密码")), \
            1)
            return
        result = yield gen.Task(self.task, username, password)
        self.finish(result, 1)

    @gen.coroutine
    def task(self, username, password):
        if User(username = username) in User:
            return self._reg_exist()    # 该用户已经注册
        try:
            if User.create(username = username, password = password):
                return self._reg_success()    # 注册成功
            return self._reg_failed()    # 注册失败
        except Exception as err:
            app_log.error(err, exc_info = 1)
            return self.error

    def _reg_exist(self):
        '''该账号已经存在'''
        return Result() \
            .status(Code_UserExist) \
            .msg(MSG.get(Code_UserExist, "该账号已经存在"))

    def _reg_success(self):
        '''注册成功'''
        return Result() \
            .status(Code_RegSuccess) \
            .msg(MSG.get(Code_RegSuccess, "注册成功"))

    def _reg_failed(self):
        '''注册失败'''
        return Result() \
            .status(Code_RegFailed) \
            .msg(MSG.get(Code_RegFailed, "未知错误注册失败"))
