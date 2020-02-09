#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time
from flask import Flask
app = Flask(__name__)


@app.route('/api', methods=['GET', 'POST'])
def api():
    time.sleep(3)
    return 'Api test！'



if __name__ == '__main__':
   # app.run(host='0.0.0.0', port=8080, debug=True)
   app.run(threaded=True)
