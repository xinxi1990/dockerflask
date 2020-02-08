import os
import time
import random
from multiprocessing import Process, Lock


# def work(n):
#
#     print('%s: %s is runing' % (n, os.getpid()))
#     time.sleep(random.random())
#     print('%s: %s is down' % (n, os.getpid()))
#
#
# if __name__ == '__main__':
#     for i in range(3):  # 利用for循环模拟多进程
#         p = Process(target=work, args=(i,))
#         p.start()



def work(lock,n):
    lock.acquire()
    print('%s: %s is runing' % (n,os.getpid()))
    time.sleep(random.random())
    print('%s: %s is down' % (n, os.getpid()))
    lock.release()

if __name__ == '__main__':

    lock = Lock()

    for i in  range(3):
        p = Process(target=work, args=(lock,i,))
        p.start()
