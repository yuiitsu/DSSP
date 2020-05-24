# -*- coding:utf-8 -*-

"""
@package:
@file: service.py
@author: yuiitsu
@time: 2020-05-24 18:39
"""
from base.service import ServiceBase
from .model import Model


class Service(ServiceBase):

    def __init__(self):
        self.model = Model()

    async def query_one(self, params):
        """
        获取一条记录
        :param params:
            params['account'] (*)
        :return:
        """
        if self.common_utils.is_empty(['account'], params):
            return self._e('PARAMS_NOT_EXIST', message_ext='account不能为空')

        data = await self.model.query_one(params)
        if not data:
            return self._e('DATA_NOT_EXIST')

        return self._rs(data)

    @ServiceBase.params_set('model', 'save_obj')
    async def create(self, params):
        """
        创建帐号
        :param params:
            params['account_type'] (*)
            params['account'] (*)
            params['password'] (*)
            params['salt'] (*)
        :return:
        """
        if self.common_utils.is_empty(['account', 'account_type', 'password', 'salt'], params):
            return self._e('PARAMS_NOT_EXIST')

        result = await self.model.create(params)
        if result is None:
            pass

        return self._rs()
