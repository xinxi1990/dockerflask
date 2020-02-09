#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
多进程
"""

import os
import time
import requests
from random import randint
from multiprocessing import Process
from multiprocessing import Pool


def coding():
    while True:
        print('开始撸代码，PID是%s' % os.getpid())
        time.sleep(randint(1, 3))
        print('写累了，不撸了，PID是%s' % os.getpid())


def play_weixin():
    while True:
        print('玩一会微信，PID是%s' % os.getpid())
        time.sleep(randint(1,2))
        print('不玩微信了，开始撸代码，PID是%s' % os.getpid())


def request_baidu(i):
    print("start request_baidu")
    r = requests.get('http://www.baidu.com')
    print(r.status_code)


if __name__ == '__main__':
    p1 = Process(target=coding)
    p2 = Process(target=coding)
    p3 = Process(target=play_weixin)
    # 启动进程
    p1.start()
    # 阻塞进程p1
    p1.join()
    # 后面p1和p2不能执行

    # # 启动进程
    p2.start()
    p3.start()

    # 主进程
    while True:
        time.sleep(3)
        print('我是主进程，PID是%s' % os.getpid())


    def do_work(thread_id):
        print('current thread {} start '.format(thread_id))
        print('开始撸代码，PID是%s' % os.getpid())
        time.sleep(3)
        print('current thread {} over'.format(thread_id))


    p = Process(target=do_work,args=[1])
    p.run()
    # p.start()
    # p.join()
    print("main thread over")
    print('我是主进程，PID是%s' % os.getpid())

    start_time = (time.clock())

    # for i in range(100):
    #     request_baidu(i)


    # for i in range(200):
    #     p = Process(target=request_baidu, args=[i])
    #     # print(p.name)
    #     p.start()
    #     # p.join()
    # for i in range(500):
    #     p.join()
    #
    # print("main thread over")
    # print('我是主进程，PID是%s' % os.getpid())

    # print (time.clock() - start_time)

    # p = Pool(4)
    # for i in range(5):
    #     p.apply_async(request_baidu, args=(i,))
    # print('Waiting for all subprocesses done...')
    # p.close()
    # p.join()
    # print('All subprocesses done.')
    #
    # print(time.clock() - start_time)