# -*- coding:utf-8 -*-

"""
@package:
@file: return_code.py
@author: yuiitsu
@time: 2020-05-24 19:55
"""
from constants.return_code import Code

Code.update({
    'JWT_GET_PARAMS_ERROR': {'code': 20101, 'msg': '必要参数缺失，shop_id/account/password'},
})
