#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-4-25
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: 长轮询获取消息
'''
from tornado import web, gen

from src.handler.base import BaseHandler
from tornado.concurrent import Future


__Author__ = "By: ヽoo悾絔℅o。\nQQ: 892768447\nEmail: 892768447@qq.com\nWeb: http://wsq.qq.com/reflow/264315676"
__Copyright__ = "Copyright (c) 2015 ヽoo悾絔℅o。"
__Version__ = "Version 1.0"

class MsgBuffer(object):

    @classmethod
    def instance(self):
        if not hasattr(self, "_instance"):
            self._instance = MsgBuffer()
        return self._instance

    def __init__(self):
        self.waiters = set()
        self.cache = []
        self.cache_size = 200

    def wait_for_messages(self, uid = None):
        result_future = Future()
        self.waiters.add(result_future)

    def cancel_wait(self, future):
        self.waiters.remove(future)
        future.set_result([])

class MsgHandler(BaseHandler):

    @web.authenticated
    @gen.coroutine
    def get(self, *args, **kwargs):
        # 得到客户端的uid
        uid = self.get_argument("uid", None)
        self.future = MsgBuffer.instance().wait_for_messages(uid = uid)
        msg = yield self.future
        if self.request.connection.stream.closed():
            return
        self.write(dict(msg = msg))

    @web.authenticated
    @gen.coroutine
    def post(self, *args, **kwargs):
        self.get(*args, **kwargs)

    def on_connection_close(self):
        # 连接关闭时清除处理
        MsgBuffer.instance().cancel_wait(self.future)
