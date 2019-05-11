# encoding=utf-8

import json

from flask import Flask
from datetime import datetime

__all__ = ["res", "ValidationError", "SupportError", "PermissionError"]

def date_handler(obj):
    if isinstance(obj, datetime):
        return obj.strftime("%Y-%m-%d %H:%M%S")

def res(result=list(), code=200, msg=""):
    """
    200: 正常处理
    203: 提交数据格式不正确
    204: 提交数据非法
    205: 没有权限
    """
    if code == 200 and not msg:
        msg = "操作完成"
    elif code == 205 and not msg:
        msg = ""
    result = {
        "code"   :      code,
        "msg"    :       msg,
        "result" :    result
    }
    return Flask.response_class(json.dumps(result, default=date_handler), mimetype="application/json")

class ValidationError(Exception):
    def __init__(self, msg="提交的数据格式错误"):
        self.msg = "Validation Error: {}".format(msg)
        Exception.__init__(self, self.msg)

class SupportError(Exception):
    def __init__(self, msg="提交的数据内容错误"):
        self.msg = "Support Error: {}".format(msg)
        Exception.__init__(self, self.msg)

class PermissionError(Exception):
    def __init__(self, msg="提交的身份认证错误"):
        self.msg = "Permission Error: {}".format(msg)
        Exception.__init__(self, self.msg)