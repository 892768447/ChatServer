#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-4-27
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: 删除好友
'''
from tornado import web, gen

from handler.base import BaseHandler, authenticated
from lib.model.relation import Relation
from lib.result import Result
from lib.status import Code_DeleteOk, MSG, Code_DeleteError


__Author__ = "By: ヽoo悾絔℅o。\nQQ: 892768447\nEmail: 892768447@qq.com\nWeb: http://wsq.qq.com/reflow/264315676"
__Copyright__ = "Copyright (c) 2015 ヽoo悾絔℅o。"
__Version__ = "Version 1.0"

class DeleteHandler(BaseHandler):

    def get(self, *args, **kwargs):
        self.render("delete.html")

    @authenticated
    @web.asynchronous
    @gen.coroutine
    def post(self, *args, **kwargs):
        uid = self.get_argument("uid", 0)
        fid = self.get_argument("fid", 0)
        result = yield gen.Task(self.task, uid, fid)
        self.finish(result, 1)

    @gen.coroutine
    def task(self, uid, fid):
        row = Relation.where(Relation.uid == uid and Relation.fid == fid).delete().execute()
        if row:
            # 删除成功
            return Result().status(Code_DeleteOk).msg(MSG.get("Code_DeleteOk", "删除成功"))
        # 删除失败
        return Result().status(Code_DeleteError).msg(MSG.get("Code_DeleteError", "删除失败"))
