# -*- coding: utf-8 -*-


import os
import requests
import json
import logging
import logzero
import time
import pymysql
from flask import g
from flask import make_response, jsonify, Blueprint, abort



blue = Blueprint('blue', __name__, url_prefix='/blue')


@blue.before_request
def get_mysql_connect():
    # 建立mysql数据库的连接
    print("建立mysql数据库的连接")
    conn = pymysql.connect(host='192.168.1.108', port=8888, user='root', password='123321', database='testcenter')
    cursor = conn.cursor()
    # 设置当前请求上下文中的应用全局对象
    g.conn = conn
    g.cursor = cursor


@blue.before_request
def create_student_table():
    # 创建student表
    print("创建student表")
    #sql = 'drop table if exists student;'
    sql = 'drop table if exists student_back;'
    sql1 = 'create table student_back(id int auto_increment, s_name varchar(10) not null, s_age int not null, primary key(id)) engine=InnoDB default charset=utf8;'
    # 执行删除表，如果student表存在则删除
    g.cursor.execute(sql)
    # 执行创建student表
    g.cursor.execute(sql1)


@blue.route('/excute_sql/')
def excute_sql():
    # 定义插入sql语句
    print("定义插入sql语句")
    sql = 'insert into student_back (s_name, s_age) values ("%s", "%s")' % ('xiaoming', '18')
    # 执行插入语句
    g.cursor.execute(sql)
    # 提交事务
    g.conn.commit()
    return '创建数据'


@blue.teardown_request
def close_mysql_connect(exception):
    # 关闭mysql数据库的连接
    print("关闭mysql数据库的连接")
    g.conn.close()


@blue.route('/ping/', methods=['GET'])
def ping():
    return jsonify({"message":"ok"})
