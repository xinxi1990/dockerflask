
"""
阻塞性定时器
"""

import os
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


def my_listener(event):
    if event.exception:
        print(event.exception)
        # 打印异常信息
        print('The job crashed')
    else:
        print('The job worked')




def my_job(id='my_job_id'):
    print(id, '-->', datetime.datetime.now())
    #scheduler.pause() # 暂停
    #scheduler.resume() # 恢复
    #scheduler.start(paused=True)
    print(1 / 0)
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), id)

def tick():
    print('Tick! The time is: %s' % datetime.now())

jobstores = {
    # 'mongo': MongoDBJobStore(),
    #'mongo': {'type': 'mongodb'},
    #'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite'),
    # 使用数据库作为存储器
    'default': MemoryJobStore()
}
executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 3
}

scheduler = BlockingScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults)
# scheduler = BlockingScheduler()
# scheduler.add_job(my_job, args=['job_interval',],id='my_job',trigger='interval', seconds=3,replace_existing=True)
scheduler.add_job(my_job, trigger='interval',seconds=3, id='my_job_id_test')

# 间隔几秒执行一次
# scheduler.remove_job('my_job_id')
# print("remove my_job_id job")
#scheduler.add_job(my_job, args=['job_cron',],id='job_cron',trigger='cron',month='4-8,11-12',hour='7-11', second='*/10',end_date='2018-05-30')
#scheduler.add_job(my_job, args=['job_once_now',],id='job_once_now')
# 立即执行
#scheduler.add_job(my_job, args=['job_date_once',],id='job_date_once',trigger='date',run_date='2020-02-13 22:36:05')
# 在某一时间执行


#scheduler.remove_job('my_job')
# scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)
# scheduler.add_job(tick, 'interval', minutes=2, id='my_job_id')
# scheduler.remove_job('my_job_id')

print(scheduler.get_jobs())
# 获取任务列表
print(scheduler.get_job(job_id="my_job_id"))
# 获取任务详情
print("#######################")
try:
    #scheduler.remove_job('my_job')  # 删除作业
    #scheduler.remove_job('my_job_id') # 删除作业
    #scheduler.pause_job('my_job_id', jobstore=None)  # 暂停作业
    ##scheduler.remove_all_jobs(jobstore=None)  # 删除所有作业
    #scheduler.resume_job('my_job_id', jobstore=None)  # 恢复作业
    changes = {"seconds":"4","trigger":'interval'}
    #scheduler.modify_job(jobstore=None, trigger='interval',seconds=4, job_id='my_job_id_test')  # 修改单个作业属性信息
    #scheduler.modify_job(job_id='my_job_id_test',seconds=4)
    # print(scheduler.get_job(job_id="my_job_id_test"))
    # print(scheduler.get_jobs())

    temp_dict = {"seconds": 5}
    temp_trigger = scheduler._create_trigger(trigger='interval', trigger_args=temp_dict)
    result = scheduler.modify_job(job_id='my_job_id_test', trigger=temp_trigger)
    # 修改任务

    #result = scheduler.reschedule_job(job_id='my_job_id_test', trigger='interval', seconds=4)
    #print(result)
    print(scheduler.get_job(job_id="my_job_id_test"))
    print("#######################")
    scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
except Exception as e:
    print(e)
try:
     scheduler.start()
except SystemExit:
    print('exit')
    exit()

scheduler.shutdown()