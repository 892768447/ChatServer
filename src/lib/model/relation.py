#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-4-27
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: 好友关系表
'''
from skylark import Model, Field


__Author__ = "By: ヽoo悾絔℅o。\nQQ: 892768447\nEmail: 892768447@qq.com\nWeb: http://wsq.qq.com/reflow/264315676"
__Copyright__ = "Copyright (c) 2015 ヽoo悾絔℅o。"
__Version__ = "Version 1.0"

class Relation(Model):
    uid = Field()    # 用户
    fid = Field()    # 好友
    gid = Field()    # 分组id
    nick = Field()    # 备注名

if __name__ == "__main__":
    import sqlite3
    import os
    from skylark import Database
    Database.set_dbapi(sqlite3)
    Database.set_autocommit(True)
    Database.config(db = os.path.abspath("../../data/data.db"))

    count = Relation.where(Relation.uid == 1).count()
    print(count)

    rel = Relation.where(Relation.uid == 0 and Relation.fid == 0).delete()
    print(rel)
    print(rel.execute())
