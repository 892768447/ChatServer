#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-5-10
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: 分组
'''
from skylark import Model, Field


__Author__ = "By: ヽoo悾絔℅o。\nQQ: 892768447\nEmail: 892768447@qq.com\nWeb: http://wsq.qq.com/reflow/264315676"
__Copyright__ = "Copyright (c) 2015 ヽoo悾絔℅o。"
__Version__ = "Version 1.0"

class Groups(Model):
    uid = Field()    # 用户id
    name = Field()    # 分类名

class GroupsWithCount(Model):
    uid = Field()    # 用户id
    name = Field()    # 分组名
    count = Field()    # 分组好友数量