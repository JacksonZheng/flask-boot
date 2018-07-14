# -*- coding:utf-8 -*-
'''
 * @Author: jackson zheng 
 * @Date: 2018-07-13 11:14:19 
 * @Last Modified by:   jackson zheng 
 * @Last Modified time: 2018-07-13 11:14:19 
 * @Desc: 
    添加配置的超级用户，并配置超级权限，可用在初始环境
'''

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

from app.models import User
from app.models.user import UserRole
from app.mongosupport.mongosupport import connect
from app import config


def get_db():
    conn_settings = {
        'db': config.MONGODB_DATABASE,
        'host': config.MONGODB_HOST,
        'port': config.MONGODB_PORT,
        'username': config.MONGODB_USERNAME,
        'password': config.MONGODB_PASSWORD
    }
    return connect(conn_settings.pop('db'), **conn_settings)


def main():
    roles = {
        '$set': {
            'roles': [UserRole.MEMBER, UserRole.ADMIN],
        }
    }
    get_db()
    for admin in config.ADMINS:
        query = {'email': admin}
        User.find_and_modify(query, roles, upsert=True)


if __name__ == '__main__':
    main()
