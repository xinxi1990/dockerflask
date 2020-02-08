


##################
# 迭代器和生成器

import sys


s = iter([1, 2, 3, 4])

print(type([1, 2, 3, 4]))

# print(type(s))
# print(s.__next__())
# print(s.__next__())
# print(s.__next__())

#
# def func():
#     for i in s:
#         print(i)
#         yield i
#
#
# f = func()
#
# while True:
#     try:
#         # print(next(f), end=" ")
#         print(f.__next__(), end=" ")
#         print(f.send(None), end=" ")
#     except StopIteration:
#         # 如果获取到最后一个的时候，再获取next就会提示StopIteration的异常了
#         sys.exit()
#
#
# ##################
# # 协程
#
# import time
#
# def consumer():
#     r = '1xx'
#     while True:
#         n = yield r
#         if not n:
#             return
#         print('[CONSUMER] 吃鸡翅 %s...' % n)
#         time.sleep(1)
#         r = '吃完啦，饱饱的了'
#
#
# def produce(customer):
#     # 启动迭代器
#     customer.__next__()
#     # 设置变量参数为0
#     n = 0
#     while n < 3:
#         n = n + 1
#         print('[PRODUCER] 做鸡翅 %s...' % n)
#         # 想customer中传递变量n，直接跳到consumer中执行
#         r = customer.send(n)
#         print('[PRODUCER] 吃鸡翅状态 return: %s' % r)
#     # 关闭消费者
#     customer.close()

"""
开始协程
<generator object consumer at 0x103b23408>
[PRODUCER] 做鸡翅 1...
[CONSUMER] 吃鸡翅 1...
[PRODUCER] 吃鸡翅状态 return: 吃完啦，饱饱的了
[PRODUCER] 做鸡翅 2...
[CONSUMER] 吃鸡翅 2...
[PRODUCER] 吃鸡翅状态 return: 吃完啦，饱饱的了
[PRODUCER] 做鸡翅 3...
[CONSUMER] 吃鸡翅 3...
[PRODUCER] 吃鸡翅状态 return: 吃完啦，饱饱的了
结束协程


区别是send()可以传递yield表达式的值进去，而next()不能传递特定的值
"""
# if __name__ == '__main__':
#     print('开始协程')
#     customer = consumer()
#     print(customer)
#     produce(customer)
#     print('结束协程')


def task_1():

    for i in range(10):
        print("current task 1 index: {}".format(i))
        yield i




def task_2(object):
    # object.__next__()
    count = 0
    while count < 8:
        object.send(None)
        print("current task 2 count: {}".format(count))
        count = count + 1
    object.close()



t1 = task_1()
print(t1)
t1 = task_2(t1)



