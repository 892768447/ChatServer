#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-4-28
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: 
'''
import asyncio
from threading import Thread


__Author__ = "By: ヽoo悾絔℅o。\nQQ: 892768447\nEmail: 892768447@qq.com\nWeb: http://wsq.qq.com/reflow/264315676"
__Copyright__ = "Copyright (c) 2015 ヽoo悾絔℅o。"
__Version__ = "Version 1.0"

class AsyncThread(Thread):

    def __init__(self, *args, **kwargs):
        super(AsyncThread, self).__init__(*args, **kwargs)
        self.setDaemon(True)
        self._loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self._loop)
        asyncio.async(self._first(), loop = self._loop)

    @property
    def loop(self):
        self._check()
        return self._loop

    def _check(self):
        if self._loop is None:
            raise RuntimeError("the loop is None")

    def __call__(self, func, *args, **kwargs):
        self._check()
        if callable(func):
            asyncio.async(func(*args, **kwargs), loop = self._loop)

    @asyncio.coroutine
    def _first(self):
        pass

    @asyncio.coroutine
    def __stop__(self):
        try:
            self._loop.stop()
        except Exception as err:
            print(err)

    def __stop(self):
        asyncio.async(self.__stop__(), loop = self._loop)

    def stop(self):
        self._check()
        self.__stop()

    def run(self):
        self._check()
        try:
            self._loop.run_forever()
        finally:
            if hasattr(self, "loop"):
                self._loop.stop()
                self._loop.close()

if __name__ == "__main__":

    @asyncio.coroutine
    def test2(time, loop):
        print("test2")
        yield from asyncio.sleep(time, loop = loop)
        print("i sleep %s s" % time)


    async = AsyncThread()
    async.start()
    async(test2, 2, async.loop)
    print(3)
    input("::")
    async.stop()
