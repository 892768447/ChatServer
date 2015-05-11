#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-4-26
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: 用户模型
'''
from skylark import Model, Field


__Author__ = "By: ヽoo悾絔℅o。\nQQ: 892768447\nEmail: 892768447@qq.com\nWeb: http://wsq.qq.com/reflow/264315676"
__Copyright__ = "Copyright (c) 2015 ヽoo悾絔℅o。"
__Version__ = "Version 1.0"

class User(Model):
    uname = Field()    # 用户名
    upass = Field()    # 密码
    head = Field()    # 头像
    sex = Field()    # 性别
    qq = Field()    # qq
    email = Field()    # 邮箱
    tel = Field()    # 电话号码
    address = Field()    # 地址
    website = Field()    # 网站地址
    rtime = Field()    # 注册时间

if __name__ == "__main__":
    import sqlite3
    import os
    from skylark import Database
    Database.set_dbapi(sqlite3)
    Database.set_autocommit(True)
    Database.config(db = os.path.abspath("../../data/data.db"))

    for u in User.select():
        print(u.data)
