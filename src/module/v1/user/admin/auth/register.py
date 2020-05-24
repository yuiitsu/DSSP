# -*- coding:utf-8 -*-

"""
API 帐号注册
@package:
@file: register.py
@author: yuiitsu
@time: 2020-05-24 22:42
"""
from base.base import Base


class Controller(Base):

    async def post(self):
        params = self.params()
        result = yield self.do_service('user.auth.service', 'register', params)
        self.out(result)
