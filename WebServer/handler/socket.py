#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-4-27
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: WebSocket
'''
from tornado import web, gen
from tornado.websocket import WebSocketHandler

from handler.base import BaseHandler
from tornado.httpclient import AsyncHTTPClient


__Author__ = "By: ヽoo悾絔℅o。\nQQ: 892768447\nEmail: 892768447@qq.com\nWeb: http://wsq.qq.com/reflow/264315676"
__Copyright__ = "Copyright (c) 2015 ヽoo悾絔℅o。"
__Version__ = "Version 1.0"

class SocketHandler(WebSocketHandler):

    def open(self, *args, **kwargs):
#         print(self.get_current_user())
#         if not self.get_current_user():
#             self.write_message("请先登录")
#             self.close()
        print("连接已经打开")
        # self.write_message("连接已经打开")

    @gen.coroutine
    def on_message(self, message):
        if self.ws_connection is None:
            return
        print("server recv: " + message)
        self.write_message("client recv: " + message)
        client = AsyncHTTPClient()
        response = yield gen.Task(client.fetch, "http://www.webtoolkit.eu/wt")
        body = response.body
        self.write_message(body)

    def on_close(self):
        print("连接关闭")
        self.clear_all_cookies()
