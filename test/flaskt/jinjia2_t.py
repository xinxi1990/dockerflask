
# encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Markup


import jinja2
from flask import request
from flask import Flask, escape, url_for,render_template

app = Flask(__name__)



@app.route('/home', methods=['GET', 'POST'])
def get_home():
    name = "mike"
    info = {'name':'mike',
            'age': '18',
            }
    return render_template('home.html',info=info)


@app.route('/homeshow', methods=['GET', 'POST'])
def get_home_show():
    return render_template('homeshow.html')


@app.route('/macro', methods=['GET', 'POST'])
def get_macro():
    return render_template('importmacro.html')



@app.route('/scores/')
def scores():
    cols = [21,34,32,67,89,43,22,13]
    return render_template('for.html',cols=cols,content_h2 = '<h2>今天你们真帅</h2>')


print(Markup('<strong>Hello %s!</strong>') % '<blink>hacker</blink>')

if __name__ == '__main__':

    app.debug = True
    app.run()