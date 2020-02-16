
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uuid
from flask import Flask
app = Flask(__name__)


@app.route('/hello/<name>/')
def hello_man(name):
    print(type(name))
    return 'hello name:%s type:%s' % (name, type(name))

@app.route('/helloint/<int:id>/')
def hello_int(id):
    print(id)
    print(type(id))
    return 'hello int: %s' % (id)

@app.route('/index/')
def index():
    return render_template('hello.html')

@app.route('/getfloat/<float:price>/')
def hello_float(price):

    return 'float: %s' % price

@app.route('/getstr/<string:name>/')
def hello_name(name):

    return 'hello name: %s' % name

@app.route('/getpath/<path:url_path>/')
def hello_path(url_path):

    return 'path: %s' % url_path

@app.route('/getuuid/')
def gello_get_uuid():
    a = uuid.uuid4()
    print(a)
    return str(a)

@app.route('/getbyuuid/<uuid:uu>/')
def hello_uuid(uu):
    return 'uu:%s' % uu

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)