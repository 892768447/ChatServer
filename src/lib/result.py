#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-4-26
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: 返回结果json格式
'''

__Author__ = "By: ヽoo悾絔℅o。\nQQ: 892768447\nEmail: 892768447@qq.com\nWeb: http://wsq.qq.com/reflow/264315676"
__Copyright__ = "Copyright (c) 2015 ヽoo悾絔℅o。"
__Version__ = "Version 1.0"

class Result(dict):

    def __init__(self, *args, **kwargs):
        super(Result, self).__init__(*args, **kwargs)

    def status(self, status = 0):
        self.__setitem__("status", status)
        return self

    def msg(self, msg = ""):
        self.__setitem__("msg", msg)
        return self

    def types(self, types = 0):
        self.__setitem__("type", types)
        return self

    def data(self, data):
        self.__setitem__("data", data)
        return self

if __name__ == "__main__":
    result = Result()
    print(result)
    b = result.status(2).msg("aaaa").types(4).data({})
    print(b)
    print(b.get("data"))
