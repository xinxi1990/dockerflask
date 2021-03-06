#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
多线程
"""

"""
import time
import threading

class DataCopy(threading.Thread):

    def __init__(self, dbname):
        super(DataCopy, self).__init__()
        self.dbName = dbname

    def run(self):

        print('Thread %s is running' % threading.current_thread().name)
        print('开始备份数据库:%s' % self.dbName)

        time.sleep(5)

        print('数据库%s备份结束' % self.dbName)
        print('Thread %s is ended' % threading.current_thread().name)



thread1 = DataCopy('database1')
thread2 = DataCopy('database2')

thread1.daemon = True
# 当定义子线程为守护线程的话，当主线程结束了，不管子线程是否执行完，都会被直接给暂停掉。默认daemon为False
thread1.start()
# start() 方法是启动一个子线程，线程名就是我们定义的name，或者默认的线程名Thread-1， Thread-2......

thread2.run()
# run() 方法并不启动一个新线程，就是在主线程中调用了一个普通函数而已。
# 线程阻塞
# 在你的子线程没有中止或者运行完之前，你的主线程都不会结束
#thread1.join()

# 线程执行结束的输出提示
print('备份结束')

"""

# import os
# import time
# import threading
#
# def task():
#
#     print(t.getName())
#     print(threading.current_thread().name)
#     print('task')
#     time.sleep(3)
#
#
#
# t = threading.Thread(target=task, name='LoopThread')
#
# t.daemon = True
#
# t.start()
#
# # t.join()
#
#
#
# print(threading.current_thread().name)


# ================================

"""
线程池
"""



#! /usr/bin/env python
# -*- coding: utf-8 -*-

import threadpool
import time

def sayhello (a):
    print("hello: "+a)
    time.sleep(2)

def main():
    global result
    seed=["a","b","c"]
    start = time.time()

    task_pool = threadpool.ThreadPool(5)
    requests = threadpool.makeRequests(sayhello,seed)

    for req in requests:
        task_pool.putRequest(req)
    task_pool.wait()
    end = time.time()
    time_m = end-start
    print("time: "+str(time_m))

    start1 = time.time()
    for each in seed:
        sayhello(each)
    end1 = time.time()
    print("time1: "+str(end1-start1))

if __name__ == '__main__':
    main()