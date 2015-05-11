#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-4-27
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: 根据id查询所有好友
'''
from skylark import Model, Field


__Author__ = "By: ヽoo悾絔℅o。\nQQ: 892768447\nEmail: 892768447@qq.com\nWeb: http://wsq.qq.com/reflow/264315676"
__Copyright__ = "Copyright (c) 2015 ヽoo悾絔℅o。"
__Version__ = "Version 1.0"

class Friends(Model):
    fid = Field()    # 好友id
    gid = Field()    # 分组id
    name = Field()    # 用户名
    head = Field()    # 头像
    nick = Field()    # 备注名

if __name__ == "__main__":
    import sqlite3
    import os
    from skylark import Database
    Database.set_dbapi(sqlite3)
    Database.set_autocommit(True)
    Database.config(db = os.path.abspath("../../data/data.db"))

    friends = Friends.at(1).limit(10, 0).select()
    print(friends)
    print(friends.sql)
    for f in friends:
        print(f.id, f.nick, f.name, f.head)
