#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-5-10
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: 分组
'''
from skylark import Model, Field, PrimaryKey


__Author__ = "By: ヽoo悾絔℅o。\nQQ: 892768447\nEmail: 892768447@qq.com\nWeb: http://wsq.qq.com/reflow/264315676"
__Copyright__ = "Copyright (c) 2015 ヽoo悾絔℅o。"
__Version__ = "Version 1.0"

class Groups(Model):
    id = PrimaryKey()
    uid = Field()    # 用户id
    name = Field()    # 分类名

class Ngroups(Model):
    uid = Field()    # 用户id
    name = Field()    # 分组名
    count = Field()    # 分组好友数量

if __name__ == "__main__":
    import sqlite3
    import os
    from skylark import Database
    Database.set_dbapi(sqlite3)
    Database.set_autocommit(True)
    Database.config(db = os.path.abspath("../../data/data.db"))

    r = Groups.where(Groups.id == "1", Groups.uid == 1).update(name = "bbbdfdfdfb").execute()
    print(r)

    r = Ngroups.select()
    for i in r:
        print(i.data)

    groups = Ngroups.where(Ngroups.uid == 1).select()
    for g in groups:
        print(g)
    print([group.data for group in groups])
