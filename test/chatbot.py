#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/connect', methods=['GET', 'POST'])
def connect():
    return 'Service is runing...'


@app.errorhandler(404)
def page_not_found(error):
    return render_template("error400.html"), 404

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)
