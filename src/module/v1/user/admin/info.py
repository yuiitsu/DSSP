# -*- coding:utf-8 -*-

"""
管理员信息
@author fuweiyi
@time 2020/6/2
"""
from base.base import Base


class Controller(Base):

    auth = (('admin', 'platform'), )

    async def get(self):
        """
        查询登录用户信息
        return data:
            {
                "admin_id": "",
                "account": "",
                "name": "",
            }
        """
        params = self.params()
        result = await self.cs('user.admin.service', 'query', params)
        self.out(result)

    async def put(self):
        """
        修改登录用户信息
        @return:
        """
        params = self.params()
        result = await self.cs('user.admin.service', 'modify_info', params)
        self.out(result)
