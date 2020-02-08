# -*- coding: utf-8 -*-

"""
学生类
"""

from views.models import *



class Student(db.Model):

    __tablename__ = 't_student'

    s_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_name = db.Column(db.String(20), unique=True)
    s_age = db.Column(db.Integer, default=18)
    s_g = db.Column(db.Integer, db.ForeignKey('t_gradle.g_id'), nullable=True)


    def __init__(self, name, age):

        self.s_name = name
        self.s_age = age
        self.s_g = None