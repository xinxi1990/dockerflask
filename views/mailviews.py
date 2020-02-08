
# -*- coding: utf-8 -*-
"""
上传文件
"""
import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
# import codecs
# print(sys.stdout.encoding)
# sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
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
from main import db,app,mail
from views.models.user import UserModels
from flask import render_template
from flask_mail import Mail, Message



new_mail = Blueprint('mail', __name__, url_prefix='/mail')


@new_mail.route("/send_mail")
def send_mail():
    """
    发送邮件， sender为发送者邮箱， recipients为接受者邮箱
    """
    print(app.config["MAIL_USERNAME"])
    message = Message("Hi!This is a test", sender=app.config["MAIL_USERNAME"], recipients=["xinxi1990@163.com"])
    message.body = "Hi!This is a test"
    message.html = "<h1>test body</h1>"
    send_email(message)
    return u"发送成功"


def send_email(msg):
    mail.send(msg)