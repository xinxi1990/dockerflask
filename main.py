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
from flask import Flask,make_response,request,redirect,url_for
from flask import Flask, session
from flask_session import Session
from flask_script import Manager
from flask import jsonify,Response,send_file
from flask import make_response, jsonify, Blueprint, abort
from configparser import ConfigParser
from flask import Flask, request
from flask import Blueprint, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from flask_sqlalchemy import SQLAlchemy



logger = setup_logger(name="backend", logfile= os.getcwd() + "/logger.log", level=logging.INFO)

# Set a custom formatter
formatter = logging.Formatter('%(name)s - %(asctime)-15s - %(levelname)s: %(message)s');
logzero.formatter(formatter)

blue = Blueprint('app_page',__name__)



class Config(object):
      """配置参数"""
      SQLALCHEMY_DATABASE_URI = "mysql://root:123321@192.168.1.104:8888/testcenter?charset=utf8"
      # 设置sqlalchemy自动跟踪数据库
      SQLALCHEMY_TRACE_MODIFICATIONS = True



def create_app():
    app = Flask(__name__)
    # SECRET_KEY 秘钥
    app.config['SECRET_KEY'] = 'secret_key'
    # app.config['SECRET_KEY'] = os.urandom(24)
    # 设置为24位的字符,每次运行服务器都是不同的，所以服务器启动一次上次的session就清除。
    # session类型为redis
    app.config['SESSION_TYPE'] = 'redis'
    app.config['SESSION_REDIS'] = Redis(host='192.168.1.104', port=6379,db=15)
    # 添加前缀
    app.config['SESSION_KEY_PREFIX'] = 'flask'
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)  # 设置session的保存时间。

    # # 加载app的第一种方式
    # se = Session()
    # se.init_app(app=app)
    # # 加载app的第二种方式
    # Session(app)
    # app.register_blueprint(blueprint=blue)

    manager = Manager(app)
    sess = Session(app)
    sess.init_app(app)

    return app

app = create_app()
app.debug = True
app.config.from_object(Config)


db = SQLAlchemy(app) #初始化数据库
db.create_all()


def get_config():
    """
    获取配置文件
    :return:
    """
    cp = ConfigParser()
    cp.read(os.path.dirname(__file__) + '/config.cfg')
    return cp


config = get_config()


# 创建蓝图
from views import appviews
app.register_blueprint(appviews.base)
