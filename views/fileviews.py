

"""
上传文件
"""

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
from flask import render_template




file = Blueprint('file', __name__, url_prefix='/file')


@file.route('/web', methods=['GET'])
def web():
    return render_template('files.html')


@file.route('/save', methods=['POST'])
def save():
    # 获取图片
    icons = request.files.get('icons')
    # 保存save(path)
    file_path = os.path.join(os.getcwd(), icons.filename)
    icons.save(file_path)
    return file_path



