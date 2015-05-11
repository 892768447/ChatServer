#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-4-25
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: 
'''
import hashlib

__Author__ = "By: ヽoo悾絔℅o。\nQQ: 892768447\nEmail: 892768447@qq.com\nWeb: http://wsq.qq.com/reflow/264315676"
__Copyright__ = "Copyright (c) 2015 ヽoo悾絔℅o。"
__Version__ = "Version 1.0"

def encrypt(data, key):
    i, j = 0, 0
    result = ""
    data_len = len(data)
    key_len = len(key)
    while (i < data_len):
        if (j > key_len - 1):
            j = j % key_len
        ch = ord(data[i]) + ord(key[j])
        if(ch > 65535):
            ch = ch % 65535
        result = result + chr(ch)
        i += 1
        j += 1
    del i, j, data_len, key_len
    return result

def decrypt(data, key):
    i, j = 0, 0
    result = ""
    data_len = len(data)
    key_len = len(key)
    while (i < data_len):
        if (j > key_len - 1):
            j = j % key_len
        ch = ord(data[i]) + 65535 - ord(key[j])
        if(ch > 65535):
            ch = ch % 65535
        result = result + chr(ch)
        i += 1
        j += 1
    del i, j, data_len, key_len
    return result

def sha512(data):
    try:
        return hashlib.sha512(data).hexdigest()
    except:
        return hashlib.sha512(data.encode()).hexdigest()

def md5(data):
    try:
        return hashlib.md5(data).hexdigest()
    except:
        return hashlib.md5(data.encode()).hexdigest()