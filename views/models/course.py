# -*- coding: utf-8 -*-


"""
学生类
"""

from views.models import *


sc = db.Table('t_sc',
                  db.Column('s_id', db.Integer, db.ForeignKey('t_student.s_id'), primary_key=True),
                  db.Column('c_id', db.Integer, db.ForeignKey('t_courses.c_id'), primary_key=True)
                  )




class Course(db.Model):

    c_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    c_name = db.Column(db.String(20), unique=True)
    students = db.relationship('Student',
                               secondary=sc,
                               backref='cou')

    __tablename__ = 't_courses'

    def __init__(self, name):

        self.c_name = name