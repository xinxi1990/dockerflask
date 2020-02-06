#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask
app = Flask(__name__)


@app.route('/api', methods=['GET', 'POST'])
def api():
	return 'Api test！'



if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)
