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
from flask import render_template


"""
钩子函数
"""


hooks = Blueprint('hooks', __name__, url_prefix='/hooks')




@hooks.route('/ping', methods=['GET'])
def ping():
    logger.info('ping')
    return 'ping ok'



@hooks.before_request
def before_request():
    print('before_request')


@hooks.after_request
def after_request(response):
    print('after_request')
    return response


@hooks.teardown_request
def teardown_request(exception):
    print('teardown_request')

@hooks.route('index/')
def index_requst():
    return 'index_requst'



