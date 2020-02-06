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
from flask import Flask,signals,render_template


# signals_new = Blueprint('signals', __name__, url_prefix='/signals')
app = Flask(__name__)

# 往信号中注册函数
def func(*args,**kwargs):
    print('触发型号',args,kwargs)
signals.request_started.connect(func)

# 触发信号： signals.request_started.send()
@app.before_first_request
def before_first1(*args,**kwargs):
    pass
@app.before_first_request
def before_first2(*args,**kwargs):
    pass

@app.before_request
def before_first3(*args,**kwargs):
    pass

@app.route('/',methods=['GET',"POST"])
def index():
    print('视图')
    return render_template('error400.html')