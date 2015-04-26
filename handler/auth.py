#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-4-25
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: 登录退出
'''
from tornado import gen
from tornado.escape import json_encode
from tornado.log import app_log
from tornado.web import HTTPError

from handler.base import BaseHandler
from lib.result import Result
from lib.status import MSG, Code_UserExist, Code_RegNoUserName, \
    Code_RegNoPassword, Code_RegSucess, Code_RegFailed
from model.user import User


__Author__ = "By: ヽoo悾絔℅o。\nQQ: 892768447\nEmail: 892768447@qq.com\nWeb: http://wsq.qq.com/reflow/264315676"
__Copyright__ = "Copyright (c) 2015 ヽoo悾絔℅o。"
__Version__ = "Version 1.0"

class AuthLoginHandler(BaseHandler):

    @gen.coroutine
    def post(self, *args, **kwargs):
        data = self.get_argument("data", None)
        if not data:
            raise HTTPError(500, "data is none")
        # 解析登录包并判断
        # 登录成功放入cookie(时间为1天)
        self.set_secure_cookie("user", json_encode(data), 1)
        self.finish("登陆成功")

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
        user = User(username = username)
        if user in User:
            # 该用户已经注册
            self.finish(Result().status(Code_UserExist).msg(MSG.get(Code_UserExist, "")), 1)
            return
        if not username:
            self.finish(Result().status(Code_RegNoUserName).msg(MSG.get(Code_RegNoUserName, "没有填写用户名")), 1)
            return
        if not password:
            self.finish(Result().status(Code_RegNoPassword).msg(MSG.get(Code_RegNoPassword, "没有填写密码")), 1)
            return
        try:
            if User.create(username = username, password = password, userhead = userhead):
                # 注册成功
                self.finish(Result().status(Code_RegSucess).msg(MSG.get(Code_RegSucess, "注册成功")), 1)
                return
            # 注册失败
            self.finish(Result().status(Code_RegFailed).msg(MSG.get(Code_RegFailed, "未知错误注册失败")), 1)
        except Exception as err:
            app_log.error(err, exc_info = 1)
