#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-4-26
@author: ヽoo悾絔℅o。
@email: 892768447@qq.com
@description: 状态码以及消息
'''

__Author__ = "By: ヽoo悾絔℅o。\nQQ: 892768447\nEmail: 892768447@qq.com\nWeb: http://wsq.qq.com/reflow/264315676"
__Copyright__ = "Copyright (c) 2015 ヽoo悾絔℅o。"
__Version__ = "Version 1.0"

Code_Error = -1    # 未知错误
Code_Ok = 0    # 无异常
Code_RegNoUserName = 1    # 没有填写用户名
Code_RegNoPassword = 2    # 没有填写密码
Code_UserExist = 3    # 账号已存在
Code_RegSuccess = 4    # 注册成功
Code_RegFailed = 5    # 注册失败
Code_LoginSuccess = 6    # 登录成功
Code_LoginFailed = 7    # 登录失败

MSG = { \
    Code_Error : "未知错误", \
    Code_Ok : "", \
    Code_UserExist : "该账号已经存在", \
    Code_RegNoUserName : "没有填写用户名", \
    Code_RegNoPassword : "没有填写密码", \
    Code_RegSuccess : "注册成功", \
    Code_RegFailed : "未知错误注册失败", \
    Code_LoginSuccess : "登录成功", \
    Code_LoginFailed : "用户不存在或者用户名密码错误", \
}

if __name__ == "__main__":
    print(Code_UserExist, MSG.get(Code_UserExist, ""))
