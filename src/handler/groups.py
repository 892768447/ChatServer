#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-5-10
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: 
'''

from tornado import web, gen
from tornado.log import app_log

from src.handler.base import BaseHandler, authenticated
from src.lib.model.groups import Groups, Ngroups
from src.lib.status import Code_Ok, Code_GroupsAddNoName, \
    Code_GroupsAddExist, Code_GroupsAddSuccess, Code_GroupsAddFailed, \
    Code_GroupsDelSuccess, Code_GroupsDelFailed, Code_GroupsModifySucess, \
    Code_GroupsModifyFailed


__Author__ = "By: ヽoo悾絔℅o。\nQQ: 892768447\nEmail: 892768447@qq.com\nWeb: http://wsq.qq.com/reflow/264315676"
__Copyright__ = "Copyright (c) 2015 ヽoo悾絔℅o。"
__Version__ = "Version 1.0"

class GetGroupsHandler(BaseHandler):
    # 获取分组

    def get(self, *args, **kwargs):
        self.render("groups.html")

    @authenticated
    @web.asynchronous
    @gen.coroutine
    def post(self, *args, **kwargs):
        uid = self.get_argument("uid", 0)
        result = yield gen.Task(self.task, uid)
        self.finish(result, 1)

    @gen.coroutine
    def task(self, uid):
        try:
            uid = int(uid)
        except Exception as err:
            app_log.error(err, exc_info = 1)
            return self.error
        try:
            groups = Ngroups.where(Ngroups.uid == uid).select()
            return self._result(Code_Ok).data([group.data for group in groups])
        except Exception as err:
            app_log.error(err, exc_info = 1)
        return self.error

class AddGroupsHandler(BaseHandler):
    # 添加分组

    def get(self, *args, **kwargs):
        self.render("groups.html")

    @authenticated
    @web.asynchronous
    @gen.coroutine
    def post(self, *args, **kwargs):
        uid = self.get_argument("uid", 0)
        name = self.get_argument("name")
        result = yield gen.Task(self.task, uid, name)
        self.finish(result, 1)

    @gen.coroutine
    def task(self, uid, name):
        try:
            uid = int(uid)
        except Exception as err:
            app_log.error(err, exc_info = 1)
            return self.error
        if not name:
            return self._result(Code_GroupsAddNoName)    # 没有填写分组名
        if Groups(uid = uid, name = name) in Groups:
            return self._result(Code_GroupsAddExist)    # 该分组已经存在
        try:
            if Groups.create(uid = uid, name = name):
                return self._result(Code_GroupsAddSuccess)    # 添加成功
            return self._result(Code_GroupsAddFailed)    # 添加失败
        except Exception as err:
            app_log.error(err, exc_info = 1)
        return self.error

class DelGroupsHandler(BaseHandler):
    # 删除分组

    def get(self, *args, **kwargs):
        self.render("groups.html")

    @authenticated
    @web.asynchronous
    @gen.coroutine
    def post(self, *args, **kwargs):
        uid = self.get_argument("uid", 0)
        gid = self.get_argument("gid", 0)
        result = yield gen.Task(self.task, uid, gid)
        self.finish(result, 1)

    @gen.coroutine
    def task(self, uid, gid):
        row = Groups.where(Groups.id == gid, Groups.uid == uid).delete().execute()
        if row:
            # 删除成功
            return self._result(Code_GroupsDelSuccess)
        # 删除失败
        return self._result(Code_GroupsDelFailed)

class ModifyGroupsHandler(BaseHandler):
    # 修改分组

    def get(self, *args, **kwargs):
        self.render("groups.html")

    @authenticated
    @web.asynchronous
    @gen.coroutine
    def post(self, *args, **kwargs):
        uid = self.get_argument("uid", 0)
        gid = self.get_argument("gid", 0)
        name = self.get_argument("name")
        result = yield gen.Task(self.task, uid, gid, name)
        self.finish(result, 1)

    @gen.coroutine
    def task(self, uid, gid, name):
        if not name:
            return self._result(Code_GroupsAddNoName)
        row = Groups.where(Groups.id == gid, Groups.uid == uid).update(name = name).execute()
        if row:
            # 修改成功
            return self._result(Code_GroupsModifySucess)
        # 修改失败
        return self._result(Code_GroupsModifyFailed)
