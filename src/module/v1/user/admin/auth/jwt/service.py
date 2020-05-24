# -*- coding:utf-8 -*-

"""
@package:
@file: service.py
@author: yuiitsu
@time: 2020-05-24 18:13
"""
from base.service import ServiceBase
from tools.jwt import JWT
from .return_code import Code


class Service(ServiceBase):

    def __init__(self):
        self.return_code = Code
        # self.model = Model()

    async def get_access_token(self, params):
        """
        获取JWT ACCESS TOKEN
        :param params:
            params['shop_id'] (*)
            params['account'] (*)
            params['password'] (*)
        :return:
        """
        if self.common_utils.is_empty(['shop_id', 'account', 'password'], params):
            raise self._e('JWT_GET_PARAMS_ERROR')

        account_res = await ServiceBase.do_service('v1.user.admin.account.service', 'query_one', {
            'shop_id': params['shop_id'],
            'account': params['account']
        })

        return self._rs({})
