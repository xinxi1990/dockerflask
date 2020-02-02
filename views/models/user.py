#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@Author  : xinxi
@Time    : 2018/1/5 16:15
@describe:

"""

from flask_login import UserMixin


from sqlalchemy import Column,Integer,String
from flask_sqlalchemy import SQLAlchemy
from main import app
from main import db




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
