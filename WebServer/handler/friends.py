#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-4-25
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: 获取好友、添加好友、删除好友、查看好友资料
'''
from handler.base import BaseHandler
from tornado.escape import json_encode

__Author__ = "By: ヽoo悾絔℅o。\nQQ: 892768447\nEmail: 892768447@qq.com\nWeb: http://wsq.qq.com/reflow/264315676"
__Copyright__ = "Copyright (c) 2015 ヽoo悾絔℅o。"
__Version__ = "Version 1.0"

class GetFriendsHandler(BaseHandler):

    def get(self, *args, **kwargs):
        username = self.get_argument("username", None)
        password = self.get_argument("password", None)
        if username == "admin":
            print(username)
            self.set_secure_cookie("user", json_encode("{'username':'%s','password':'%s'}" % (username, password)), 1)

        print(self.get_current_user())
        self.finish('''
            <html>
                <body>
                    <form action="/friends" method="post">
                        <input type="text" name="username" /><br />
                        <input type="text" name="password" /><br />
                        <input type="hidden" name="_xsrf" value="%s" /><br />
                        <input type="submit" value="提交" /><br />
                        <input type="reset" value="重置" /><br />
                    </form>
                </body>
            </html>
        ''' % self.xsrf_token.decode())

    def post(self, *args, **kwargs):
        self.get(*args, **kwargs)
