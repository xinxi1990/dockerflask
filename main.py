# -*- coding: utf-8 -*-


import os
import requests
import json
import logging
import logzero
import time
import copy
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
from flask_login import LoginManager, login_required, login_user, logout_user,current_user
# from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail, Message



logger = setup_logger(name="backend", logfile= os.getcwd() + "/logger.log", level=logging.INFO)

# Set a custom formatter
formatter = logging.Formatter('%(name)s - %(asctime)-15s - %(levelname)s: %(message)s');
logzero.formatter(formatter)

blue = Blueprint('app_page',__name__)



class Config(object):
      """配置参数"""
      SQLALCHEMY_DATABASE_URI = "mysql://root:123321@192.168.1.108:8888/testcenter?charset=utf8"
      #设置sqlalchemy自动跟踪数据库
      SQLALCHEMY_TRACE_MODIFICATIONS = True

      DATABASE = 'flask.db'  # 数据库文件地址

      #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'


def create_mail():
    app.config.update(
        DEBUG=True,
        MAIL_SERVER='smtp.126.com',
        MAIL_PROT=25,
        MAIL_USE_TLS=True,
        MAIL_USE_SSL=False,
        MAIL_USERNAME='autotestin@126.com',
        MAIL_PASSWORD=os.environ.get('mail_password'),
        MAIL_DEBUG=True

    )
    print(os.environ.get('mail_password'))



def create_app():
    app = Flask(__name__)
    # SECRET_KEY 秘钥
    app.config['SECRET_KEY'] = 'secret_key'
    # app.config['SECRET_KEY'] = os.urandom(24)
    # 设置为24位的字符,每次运行服务器都是不同的，所以服务器启动一次上次的session就清除。
    # session类型为redis
    app.config['SESSION_TYPE'] = 'redis'
    app.config['SESSION_REDIS'] = Redis(host='192.168.1.108', port=6379,db=15)
    # 添加前缀
    app.config['SESSION_KEY_PREFIX'] = 'flask'
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)  # 设置session的保存时间。
    app.config['SECRET_KEY'] = '11111111'
    # # 加载app的第一种方式
    # se = Session()
    # se.init_app(app=app)
    # # 加载app的第二种方式
    # Session(app)
    # app.register_blueprint(blueprint=blue)

    manager = Manager(app)
    sess = Session(app)
    sess.init_app(app)
    app.debug = True
    # toolbar = DebugToolbarExtension(app)
    return app

app = create_app()
app.debug = True
app.config.from_object(Config)


db = SQLAlchemy(app) #初始化数据库
db.create_all()

create_mail() # 初始化邮件配置
mail = Mail(app)


# 获取登录管理对象
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "app.login"
login_manager.login_message = 'Unauthorized User'
# 设置闪现的错误消息的类别
login_manager.login_message_category = "info"

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
from views import loginviews
from views import studentviews
from views import hooksviews
from views import gviews
from views import signalsviews
from views import fileviews
from views import mailviews
app.register_blueprint(appviews.base)
app.register_blueprint(loginviews.uer_login)
app.register_blueprint(studentviews.student)
app.register_blueprint(hooksviews.hooks)
app.register_blueprint(gviews.blue)
app.register_blueprint(fileviews.file)
app.register_blueprint(mailviews.new_mail)
# app.register_blueprint(signalsviews.app)


@app.route('/ping', methods=['GET'])
def ping():
    logger.info('ping')
    return 'ping ok'



@app.before_request
def before_request():
    print('before_request')


@app.after_request
def after_request(response):
    print('after_request')
    result = copy.copy(response.response)
    try:
        if isinstance(result[0], bytes):
            result[0] = bytes.decode(result[0])
        logger.info('url:{} ,method:{},返回数据:{}'.format(request.url, request.method, json.loads(result[0])))
    except Exception as e:
        logger.info(e)
        logger.info('url:{} ,method:{}'.format(request.url, request.method))
    return response


@app.teardown_request
def teardown_request(exception):
    print('teardown_request')


# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template("error400.html"), 404
#
#
# @app.errorhander(500)
# def server_error(error):
#     return render_template("error505.html"), 500