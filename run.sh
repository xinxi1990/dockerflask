#!/bin/bash
cd /
echo "current path: "`pwd`
#export FLASK_APP=app.py
#flask run -h 0.0.0.0
gunicorn -w 1 -b 0.0.0.0:5000 manage:app