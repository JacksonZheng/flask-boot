# -*- coding: utf-8 -*-
"""
    test_crud
    ~~~~~~~~~~~~~~

    Test cases for crud.

    :copyright: (c) 2018 by fengweimin.
    :date: 2018/5/15
"""

from app.models import User


def test_user(app):
    # Init
    assert User.delete_many({})
    assert User.count({}) == 0
    # C
    user = User()
    user.name = u'test'
    user.email = u'test@test.com'
    user.password = u'test'
    user.save()
    assert User.count({}) == 1
    # R
    assert User.find_one({'name': u'test'}).name == u'test'
    # U
    user.name = u'test1'
    user.save()
    assert User.find_one({'name': u'test1'}).name == u'test1'
    # D
    assert user.delete()
    # Verify
    assert User.count({}) == 0
