

from views.models import *

"""
学生类
"""


class Gradle(db.Model):

    __tablename__ = 't_gradle'

    g_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    g_name = db.Column(db.String(20), unique=True)



    def __init__(self, name, age):

        self.g_id = name
        self.s_age = g_name
