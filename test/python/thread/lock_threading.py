#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
线程锁
通过上面的结果比较可以知道，当多线程中需要“独占资源”的时候，要使用锁来控制，防止多个线程同时占用资源而出现其他异常
使用锁的时候就调用acquire()方法，以此告诉其他线程，我正在占用该资源，你们要等会；待使用资源后需要释放资源的时候就调用release()方法，
告诉其他线程，我已经完成使用该资源了，其他人可以过来使用了
"""


# ======================================
# 线进程操作

import threading
import time

lock = threading.Lock()
l = []


def test1(n):
    lock.acquire()
    l.append(n)
    print(l)
    lock.release()
    """
    [0]
    [0, 1]
    [0, 1, 2]
    [0, 1, 2, 3]
    [0, 1, 2, 3, 4]
    [0, 1, 2, 3, 4, 5]
    [0, 1, 2, 3, 4, 5, 6]
    [0, 1, 2, 3, 4, 5, 6, 7]
    [0, 1, 2, 3, 4, 5, 6, 7, 8]
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """

def test(n):
    l.append(n)
    print(l)


def main():
    for i in xrange(0, 10):
        th = threading.Thread(target=test, args=(i,))
        th.start()
    """
    [0]
    [0, 1]
    [0, 1, 2]
    [0, 1, 2, 3]
    [0, 1[0, , 2, 31, 2[, 04, , , 135, , 26, 4][, 0, , 
    3, 4, 5, 6, 7]
    5, 6, 71], 
    2, 3, 4, 5, 6, 7][0
    , [1, 2, 3, 4, 5, 6, 7, 8, 9]
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """


# ======================================
# 多进程操作

from multiprocessing import Process
import time

def process_test(n):
    l.append(n)
    print(l)
    """
    [0]
    [1]
    [2]
    [3]
    [4]
    [5]
    [6]
    [7]
    [8]
    [9]     
    """

def process_main():
    for i in xrange(0, 10):
        th = Process(target=process_test, args=(i,))
        th.start()



if __name__ == '__main__':
    process_main()