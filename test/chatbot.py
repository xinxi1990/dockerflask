#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask
from flask import render_template
from flask_debugtoolbar import DebugToolbarExtension
app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'TTC'

toolbar = DebugToolbarExtension()
toolbar.init_app(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False



@app.route('/connect', methods=['GET', 'POST'])
def connect():
    print("connect")
    return 'Service is runing...'


@app.route('/html', methods=['GET', 'POST'])
def html():
    return render_template('login.html')



@app.errorhandler(404)
def page_not_found(error):
    return render_template("error400.html"), 404

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)
