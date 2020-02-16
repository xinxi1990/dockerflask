#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_apscheduler import APScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
app = Flask(__name__)


import pysnooper



class Config(object):
    JOBS = [
        {
            'id': 'job2',
            'func': 'flask_apscheduler_t:job1',
            'args': (1, 2),
            'trigger': 'interval',
            'seconds': 10
        }
    ]

    # SCHEDULER_JOBSTORES = {
    #     'default': SQLAlchemyJobStore(url='sqlite:///flask_jobs.sqlite')
    # }

    SCHEDULER_EXECUTORS = {
        'default': {'type': 'threadpool', 'max_workers': 20}
    }

    SCHEDULER_JOB_DEFAULTS = {
        'coalesce': False,
        'max_instances': 3
    }

    SCHEDULER_API_ENABLED = True

@pysnooper.snoop("debug.log")
def job1(a, b):
    print(str(a) + ' ' + str(b))
    job2()


@pysnooper.snoop()
def job2():
    print(3)


if __name__ == '__main__':
    app.config.from_object(Config())
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()
    app.run(host='0.0.0.0', port=5000, debug=True)



# import numpy as np
# import pysnooper
#
#
# @pysnooper.snoop()
# def one(number):
#     mat = []
#     while number:
#         mat.append(np.random.normal(0, 1))
#         number -= 1
#     return mat
#
# one(3)
