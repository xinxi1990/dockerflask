

from flask import Flask, request
import os
import requests
import json
import logging
import logzero
import time
from logzero import setup_logger
from werkzeug.utils import secure_filename
from flask import Flask,make_response,request
from flask import jsonify,Response,send_file
from flask import make_response, jsonify, Blueprint, abort
from configparser import ConfigParser
app = Flask(__name__)

logger= setup_logger(name="backend", logfile= os.getcwd() + "/logger.log", level=logging.INFO)

# Set a custom formatter
formatter = logging.Formatter('%(name)s - %(asctime)-15s - %(levelname)s: %(message)s');
logzero.formatter(formatter)


def get_config():
    """
    获取配置文件
    :return:
    """
    cp = ConfigParser()
    cp.read(os.path.dirname(__file__) + '/config.cfg')
    return cp


config = get_config()


@app.route('/ping', methods=['GET'])
def ping():
    logger.info('ping')
    return 'ping ok'



@app.route('/')
def hello_world():
    return 'Hello World!'



@app.route('/uploadfile', methods=['POST', 'GET'])
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



@app.route('/<filedir>/<filename>', methods=['GET','POST'])
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



if __name__ == '__main__':
    app.run(debug=True)
