# -*- coding: utf-8 -*-


import os
import requests
import json
import logging
import logzero
import time
from redis import Redis
from logzero import setup_logger
from datetime import timedelta
from werkzeug.utils import secure_filename
from flask import Flask,make_response,request,redirect,url_for,flash
from flask import Flask, session
from flask_session import Session
from flask_script import Manager
from flask import jsonify,Response,send_file
from flask import make_response, jsonify, Blueprint, abort
from configparser import ConfigParser
from flask import Flask, request
from flask import Blueprint, render_template, abort
from views.form.userform import UserForm
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import LoginManager, login_required, login_user, logout_user,current_user
from flask import Flask, flash, get_flashed_messages
from flask_sqlalchemy import SQLAlchemy
from main import config
from main import logger
from main import db,app
from views.models.user import UserModels
from views.models.course import Course
from views.models.student import Student
from views.models.gradle import Gradle
from views.models.course import sc



student = Blueprint('student', __name__, url_prefix='/student')




@student.route('/ping', methods=['GET'])
def ping():
    logger.info('ping')
    return 'ping ok'



@student.route('/addstudent/<string:name>/<int:age>', methods=['GET'])
def add_student(name,age):
    student = Student(name=name,age=age)
    db.session.add(student)
    db.session.commit()
    return 'add student ok!'



@student.route('/addcourse/<string:coursename>', methods=['GET'])
def add_course(coursename):
    course = Course(name=coursename)
    db.session.add(course)
    db.session.commit()
    return 'add course ok!'



@student.route('/addsc/<int:userid>/<int:courseid>', methods=['GET'])
def add_sc(userid,courseid):
    # userid = request.form.get('userid')
    # courseid = request.form.get('courseid')
    print(userid)
    print(courseid)
    stu = Student.query.get(userid)
    cou = Course.query.get(courseid)
    cou.students.append(stu) # 两个表关联起来
    db.session.add(cou)
    db.session.commit()
    return 'addsc ok!'


@student.route('/delsc/<int:userid>/<int:courseid>', methods=['GET'])
def del_sc(userid,courseid):
    # userid = request.form.get('userid')
    # courseid = request.form.get('courseid')
    print(userid)
    print(courseid)
    stu = Student.query.get(userid)
    cou = Course.query.get(courseid)
    cou.students.remove(stu)
    db.session.commit()
    return 'delsc ok!'


@student.route('/getcourse/<int:courseid>', methods=['GET'])
def get_course(courseid):
    """
    通过课程查询学生
    :param courseid:
    :return:
    """
    cou = Course.query.get(courseid)
    stus = cou.students
    print('#############')
    # print(type(stus))
    for stu in stus:
        print(stu.s_name)
        return stu.s_name
    # print(dir(stus))
    # print(vars(stus))
    # print((stus.__repr__))
    # print('#############')
    # return 'getcourse ok!'


@student.route('/getstudent/<int:userid>', methods=['GET'])
def get_student(userid):
    """
    通过学生查询课程
    :param courseid:
    :return:
    """
    stu = Student.query.get(id)
    cous = stu.cou
    print('#############')
    # print(type(stus))
    for con in cous:
        print(con.c_name)
        return con.c_name
    # print(dir(stus))
    # print(vars(stus))
    # print((stus.__repr__))
    # print('#############')
    # return 'getcourse ok!'