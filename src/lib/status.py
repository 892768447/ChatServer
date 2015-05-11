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
Code_LoginNoUsername = 6    # 没有输入用户名
Code_LoginNoPassword = 7    # 没有输入密码
Code_LoginSuccess = 8    # 登录成功
Code_LoginFailed = 9    # 登录失败
Code_TokenError = 10    # token过期,不正确,不存在
Code_DeleteOk = 11    # 删除成功
Code_DeleteError = 12    # 删除失败
Code_GroupsAddNoName = 13    # 没有填写分组名
Code_GroupsAddExist = 14    # 该分组已存在
Code_GroupsAddSuccess = 15    # 添加分组成功
Code_GroupsAddFailed = 16    # 添加分组失败
Code_GroupsDelSuccess = 17    # 删除分组成功
Code_GroupsDelFailed = 18    # 删除分组失败

MSG = { \
    Code_Error : "未知错误", \
    Code_Ok : "", \
    Code_UserExist : "该账号已经存在", \
    Code_RegNoUserName : "没有填写用户名", \
    Code_RegNoPassword : "没有填写密码", \
    Code_RegSuccess : "注册成功", \
    Code_RegFailed : "未知错误注册失败", \
    Code_LoginNoUsername : "没有输入用户名", \
    Code_LoginNoPassword : "没有输入密码", \
    Code_LoginSuccess : "登录成功", \
    Code_LoginFailed : "用户不存在或者用户名密码错误", \
    Code_TokenError : "token有误", \
    Code_DeleteOk : "删除成功", \
    Code_DeleteError : "删除失败", \
    Code_GroupsAddNoName : "没有填写分组名", \
    Code_GroupsAddExist : "该分组已存在", \
    Code_GroupsAddSuccess : "添加分组成功", \
    Code_GroupsAddFailed : "添加分组失败", \
}

if __name__ == "__main__":
    print(Code_UserExist, MSG.get(Code_UserExist, ""))
