#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-4-25
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: 登录退出
'''

from tornado.log import app_log

from DbServer.handler.base import BaseHandler
from DbServer.model.user import User
from lib.result import Result
from lib.status import Code_LoginSuccess, MSG, Code_LoginFailed, \
    Code_UserExist, Code_RegSuccess, \
    Code_RegFailed


__Author__ = "By: ヽoo悾絔℅o。\nQQ: 892768447\nEmail: 892768447@qq.com\nWeb: http://wsq.qq.com/reflow/264315676"
__Copyright__ = "Copyright (c) 2015 ヽoo悾絔℅o。"
__Version__ = "Version 1.0"

class AuthLoginHandler(BaseHandler):

    def post(self, *args, **kwargs):
        self.get(*args, **kwargs)

    def get(self, *args, **kwargs):
        username = self.get_argument("username", None)
        password = self.get_argument("password", None)
        # 从数据库中查询该用户
        user = User.findone(username = username, password = password)
        if user:
            # 登录成功
            self._login_success(user)
            return
        self._login_failed()

    def _login_success(self, user):
        '''登录成功'''
        self.finish(Result() \
            .status(Code_LoginSuccess) \
            .msg(MSG.get(Code_LoginSuccess, "登录成功")) \
            .data(dict(\
                uid = user.id, \
                name = user.username, \
                head = user.userhead, \
            )), \
        1)

    def _login_failed(self):
        '''登录失败'''
        self.finish(Result() \
            .status(Code_LoginFailed) \
            .msg(MSG.get(Code_LoginFailed, "用户不存在或者用户名密码错误")), \
        1)

class AuthRegisterHandler(BaseHandler):

    def post(self, *args, **kwargs):
        self.get(*args, **kwargs)

    def get(self, *args, **kwargs):
        username = self.get_argument("username", None)
        password = self.get_argument("password", None)
        user = User(username = username)
        if user in User:
            self._reg_exist()    # 该用户已经注册
            return
        try:
            if User.create(username = username, password = password):
                self._reg_success()    # 注册成功
                return
            self._reg_failed()    # 注册失败
        except Exception as err:
            app_log.error(err, exc_info = 1)

    def _reg_exist(self):
        '''该账号已经存在'''
        self.finish(Result() \
            .status(Code_UserExist) \
            .msg(MSG.get(Code_UserExist, "该账号已经存在")), \
        1)

    def _reg_success(self):
        '''注册成功'''
        self.finish(Result() \
            .status(Code_RegSuccess) \
            .msg(MSG.get(Code_RegSuccess, "注册成功")), \
        1)

    def _reg_failed(self):
        '''注册失败'''
        self.finish(Result() \
            .status(Code_RegFailed) \
            .msg(MSG.get(Code_RegFailed, "未知错误注册失败")), \
        1)
