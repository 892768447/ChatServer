#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-4-25
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: 登录退出
'''

from tornado.log import app_log

from handler.base import BaseHandler
from lib.result import Result
from lib.status import MSG, Code_UserExist, Code_RegNoUserName, \
    Code_RegNoPassword, Code_RegSuccess, Code_RegFailed, Code_LoginSuccess, \
    Code_LoginFailed
from model.user import User
from tornado.escape import json_encode


__Author__ = "By: ヽoo悾絔℅o。\nQQ: 892768447\nEmail: 892768447@qq.com\nWeb: http://wsq.qq.com/reflow/264315676"
__Copyright__ = "Copyright (c) 2015 ヽoo悾絔℅o。"
__Version__ = "Version 1.0"

class AuthLoginHandler(BaseHandler):

    def get(self, *args, **kwargs):
        self.render("login.html")

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
        user = User.findone(username = username, password = password)
        if user:
            # 登录成功
            self.finish(Result() \
                .status(Code_LoginSuccess) \
                .msg(MSG.get(Code_LoginSuccess, "登录成功")) \
                .data(dict(\
                    uid = user.id, \
                    name = user.username, \
                    head = user.userhead, \
                )), \
            1)
            # 登录成功放入cookie(时间为1天)
            self.set_secure_cookie("user", "aaaa")
            print(self.get_secure_cookie("user"))
            return
        self.finish(Result() \
            .status(Code_LoginFailed) \
            .msg(MSG.get(Code_LoginFailed, "用户不存在或者用户名密码错误")), \
        1)

class AuthLogoutHandler(BaseHandler):

    def get(self, *args, **kwargs):
        self.clear_cookie("user")
        self.write("注销")

class AuthRegisterHandler(BaseHandler):

    def get(self, *args, **kwargs):
        self.render("reg.html")

    def post(self, *args, **kwargs):
        username = self.get_argument("username", None)
        password = self.get_argument("password", None)
        userhead = self.get_argument("userhead", None)
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
        user = User(username = username)
        if user in User:
            # 该用户已经注册
            self.finish(Result() \
                .status(Code_UserExist) \
                .msg(MSG.get(Code_UserExist, "")), \
            1)
            return
        try:
            if User.create(username = username, password = password, userhead = userhead):
                # 注册成功
                self.finish(Result() \
                    .status(Code_RegSuccess) \
                    .msg(MSG.get(Code_RegSuccess, "注册成功")), \
                1)
                return
            # 注册失败
            self.finish(Result() \
                .status(Code_RegFailed) \
                .msg(MSG.get(Code_RegFailed, "未知错误注册失败")), \
            1)
        except Exception as err:
            app_log.error(err, exc_info = 1)
