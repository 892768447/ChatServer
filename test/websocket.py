#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-4-27
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: WebSocket测试
'''
from threading import Thread

from tornado import gen
from tornado.ioloop import IOLoop
from tornado.websocket import websocket_connect


__Author__ = "By: ヽoo悾絔℅o。\nQQ: 892768447\nEmail: 892768447@qq.com\nWeb: http://wsq.qq.com/reflow/264315676"
__Copyright__ = "Copyright (c) 2015 ヽoo悾絔℅o。"
__Version__ = "Version 1.0"

class Client(Thread):

    def __init__(self, *args, **kwargs):
        super(Client, self).__init__(*args, **kwargs)
        self.io_loop = IOLoop.instance()
        self.url = None
        self.callback = None
        self.connect_timeout = None
        self.on_message_callback = None
        self.compression_options = None

    def init(self, url, callback = None, connect_timeout = None,
             on_message_callback = None, compression_options = None):
        self.url = url
        self.callback = callback
        self.connect_timeout = connect_timeout
        self.on_message_callback = on_message_callback
        self.compression_options = compression_options

    def stop(self):
        self.io_loop.stop()

    def run(self):
        # self.io_loop.r.run_sync(self._connect)
        self._connect()
        self.io_loop.start()

    def send(self, data):
        if hasattr(self, "_ws"):
            self._ws.write_message(data)

    @gen.coroutine
    def _connect(self):
        try:
            self._ws = yield websocket_connect(url = self.url, io_loop = self.io_loop,
            callback = self.callback, connect_timeout = self.connect_timeout,
            on_message_callback = self.on_message_callback, compression_options = self.compression_options)
        except Exception as err:
            print(err)


@gen.coroutine
def message_callback(data):
    print("on_message_callback: ", data)

client = Client()
client.init(url = "ws://127.0.0.1:8000/socket", on_message_callback = message_callback)
client.start()
while 1:
    data = input("---")
    if data == "exit":
        break
    elif data:
        client.send(data)
client.stop()

# @gen.coroutine
# def test():
#     ws = yield websocket_connect("ws://127.0.0.1:8000/socket")
#     while 1:
#         data = input()
#         if data:
#             ws.write_message(data)
#             msg = yield ws.read_message()
#             print(msg)
#         else:
#             break
#     ws.close()
#
#
# IOLoop.instance().run_sync(test)


