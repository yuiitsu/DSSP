# -*- coding:utf-8 -*-

"""
获取Access Token API
@package:
@file: token.py
@author: yuiitsu
@time: 2020-05-24 18:14

request body:
    {
        account: 帐户名(*)
        password: 密码(*)
        shop_id: 店铺ID. 本系统支持多店铺，所以，如果指定shop_id，将直接登录到该店铺下。如果不指定，待续.
        user_type: 类型，buyer/seller，不传默认为seller
    }

return:
    {
        access_token: 'JWT token',
        expires_in: 7200,
        refresh_expires_in: 2592000
    }
"""
from base.base import Base


class Controller(Base):

    async def post(self):
        params = self.params()
        result = yield self.do_service('user.auth.jwt.service', 'get_access_token', params)
        if result['code'] != 0:
            self.out(result)
            return

        # encoded = self.jwt_encode(result['data'])
        # result['data'] = {
        #     'access_token': encoded,
        #     'expires_in': result['data']['exp'],
        #     'refresh_expires_in': result['data']['refresh_exp'],
        #     'created_at': result['data']['iat'],
        #     'shop_id': result['data'].get('shop_id', ''),
        #     'shop_name': result['data'].get('shop_name', ''),
        # }
        self.out(result)
