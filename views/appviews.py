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
from flask_sqlalchemy import SQLAlchemy
from main import config
from main import logger
from main import db,app
from views.models.user import UserModels

base = Blueprint('app', __name__, url_prefix='/app')




@base.route('/ping', methods=['GET'])
def ping():
    logger.info('ping')
    return 'ping ok'



@base.route('/')
def hello_world():
    return 'Hello World!'



@base.route('/uploadfile', methods=['POST', 'GET'])
def upload_file():
    try:
        params = request.form.to_dict()
        f = request.files['file']
        base_path = os.path.dirname(__file__)  # 当前文件所在路径
        file_name = '{filename}'.format(filename=secure_filename(f.filename))
        dir_path = os.path.join(base_path, 'files')
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        create_time = time.strftime("%Y%m%d%H%M%S")
        file_path = 'files/{create_time}_{file_name}'.format(create_time=create_time,file_name=file_name)
        upload_path = os.path.join(base_path, file_path)
        f.save(upload_path)
        params['file_path'] = '/{}'.format(file_path)
        return jsonify({"code": 0, "msg": "上传成功", "file_path": '{}/{}'.format(config.get('config', 'backendDomain'),file_path)})
    except Exception as e:
        logger.error(e)
        logger.error('发生了错误')
        abort(500)



@base.route('/<filedir>/<filename>', methods=['GET','POST'])
def download_file(filedir,filename):
    base_path = os.path.dirname(__file__)
    try:
        file_path = base_path + '/{filedir}/{filename}'.format(filedir=filedir,filename=filename)
        logger.info("下载文件路径: " + file_path)
        return send_file(file_path)
    except Exception as e:
        logger.error(e)
        logger.error("发生了错误")
        abort(500)



# @app.route('/login/', methods=['GET', 'POST'])
# def login():
#     if request.method == 'GET':
#         username = session.get('username')
#         return render_template('login.html', username=username)
#     else:
#         username = request.form.get('username')
#         session['username'] = username
#
#         #return redirect(url_for('first.login'))
#         return redirect('http://www.baidu.com')



#设置session
@base.route('/set/')
def set():
    session['username'] = 'value'
    return 'ok'


#获取session
@base.route('/get/')
def get():
    return  session.get('username')


#删除session
@base.route('/delete/')
def delete():
    logger.info(session.get('username'))
    session.pop('username')
    logger.info(session.get('username'))
    return 'delete'


#清楚session
@base.route('/clear/')
def clear():
    logger.info(session.get('username'))
    session.clear()
    logger.info(session.get('username'))
    return 'clear'


# 集成父模版
@base.route('/extentds/', methods=['GET', 'POST'])
def extentds():
    return render_template("extentds.html")



@base.route('/register/', methods=['GET', 'POST'])
def register():
    form = UserForm()
    if request.method == 'GET':
        return render_template('register.html', form=form)

    if request.method == 'POST':
        # 判断表单中的数据是否通过验证
        if form.validate_on_submit():
            # 获取验证通过后的数据
            username = form.username.data
            password = form.password.data
            password2 = form.password.data
            # 保存
            user = UserModels(username,password,password2)
            user.username = username
            user.password = generate_password_hash(password)
            # user.save()
            logger.info("准备保存到数据库...")
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('app.login'))
        return render_template('register.html', form=form)



# @base.route('/login')
# def login():
#     logger.info("login")
#     return render_template('login.html')



@base.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # 校验用户名和密码是否填写完成
        if not all([username, password]):
            return render_template('login.html')
        # 通过用户名获取用户对象
        user = UserModels.query.filter_by(username=username).first()
        print(user)
        # 校验密码是否正确
        if check_password_hash(user.password, password):
            # 实现登录
            # login_user()能够将已登录并通过load_user()的用户对应的User对象保存在session中
            # 在session中会创建一个键值对，key为user_id，value为当前登录用户的id值
            # 如果希望应用记住用户的登录状态, 只需要为 login_user()的形参 remember 传入 True 实参就可以了.
            login_user(user)
            print("########## login over #########")
            return redirect(url_for('app.index'))
        else:
            flash('用户名或者密码错误')

        return redirect(url_for('index'))



@base.route('/index/')
@login_required
def index():
    print("####### index ############")
    return render_template('index.html')




# @base.route('/logout', methods=['POST'])
# def logout():
#     try:
#         logout_user()
#         results = {}
#         results['code'] = 0
#         results['msg'] = '退出成功'
#         response = json.dumps(results, indent=4)
#         return make_response(response)
#     except Exception as e:
#         logger.error('发生了错误，error: {}'.format(e))
#         abort(500)


# 退出
@base.route('/logout/', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))