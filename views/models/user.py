#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
@Author  : xinxi
@Time    : 2018/1/5 16:15
@describe:

"""

from views.models import *




class UserModels(db.Model, UserMixin):

    __tablename__ = 't_user'

    # 将id设置为主键，并且默认是自增长的
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(String(3000), default='未知')
    password = db.Column(String(3000), default='未知')
    password2 = db.Column(String(3000), default='未知')


    def __init__(self, username=None, password=None, password2=None):
        self.username = username
        self.password = password
        self.password2 = password2

    def todict(self):
        return self.__dict__


    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)


@login_manager.user_loader
def load_user(user_id):
    # 必须编写一个函数用于从数据库加载用户。
    # 这个函数在login_user(user)存储当前登录用户到session中时，会被调用
    # 在每次访问地址的时候都被被调用，用于向请求上下文中绑定当前登录的用户信息
    return UserModels.query.get(user_id)



