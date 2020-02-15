"""
后台性定时器
"""

import os
import time
import datetime
from pytz import utc
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR

import logging
logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.DEBUG)


def my_job(id='my_job_id'):
    print(id, '-->', datetime.datetime.now())
    #scheduler.pause() # 暂停
    #scheduler.resume() # 恢复
    #scheduler.start(paused=True)
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), id)

scheduler = BackgroundScheduler()
scheduler.add_job(my_job, trigger='interval',seconds=1, id='my_job_id_test')
scheduler.start()




def start_task():
    task_time = 100
    for i in range(task_time):
        scheduler.pause()
        print("暂停任务")
        print(task_time)
        yield
        task_time = task_time - 10
        time.sleep(10)
        scheduler.resume()
        print("恢复任务")
        scheduler.shutdown()

task = start_task()

while True:
    task.__next__()
