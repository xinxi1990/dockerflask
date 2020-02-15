


"""
从Python 3.5开始引入了新的语法async和await，可以让coroutine的代码更简洁易读.
coroutine 异步
"""

import asyncio
# import requests
import time
import requests_async as requests


async def hello():
    print("Hello world!")
    r = await asyncio.sleep(1)
    print("Hello again!")


"""
异步网络请求
"""
async def post_requests(url):
    print("Hello world!")
    async with requests.Session() as session:
        print("create Session statr")
        response = await session.get('https://example.org')
        print("create Session over")
        print(response.status_code)
        # print(response.text)


# async def async_function():
#     asyncio.sleep(1)
#     return 1

# """
# 异步函数,返回协程对象
# """
# async def async_function():
#     print('Number:', 1)
#     return 1
#
#
# async def await_coroutine():
#     result = await async_function()
#     print(result)


# loop = asyncio.get_event_loop()
# # 执行coroutine
# print("#####################")
# loop.run_until_complete(hello())
# loop.close()


# =================================



# loop = asyncio.get_event_loop()
# tasks = [post_requests(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()


#print(await_coroutine().send(None))
#
# coroutine =  async_function()
#
# loop = asyncio.get_event_loop()
# # task = loop.create_task(coroutine)
# task = asyncio.ensure_future(coroutine)
# print('Task:', task)
# loop.run_until_complete(task)
# print('Task:', task)
# print('After calling loop')
#
# import asyncio
# # import requests
#
#
# async def post_requests():
#     print("Hello world!")
#     async with requests.Session() as session:
#         print("create Session statr")
#         response = await session.get('https://example.org')
#         print("create Session over")
#         print(response.status_code)
#         # print(response.text)
#
#
# async def post_request():
#    r = requests.get('https://example.org')
#    reps = await get_response(r)
#    print(r.status_code)
#    print("post_request over")


#
# async def get_response(response):
#     print("get_response over")
#     print(response.status_code)
#
#
# def callback(task):
#     print('Status:', task.result())
#
#
# tasks = [post_requests() for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))
# print('Task:', tasks)


# async def async_function():
#     print('Number:', 1)
#     r = requests.get('http://www.baidu.com')
#     return r
#
# def callback(task):
#     print('Status:', task.result())
#
#
# coroutine = async_function()

# loop = asyncio.get_event_loop()
# task = loop.create_task(coroutine)
# print('Task:', task)
# loop.run_until_complete(task)
# print('Task:', task)
# print('After calling loop')


# task = asyncio.ensure_future(coroutine)
# print('Task:', task)
# loop = asyncio.get_event_loop()
# loop.run_until_complete(task)
# print('Task:', task)
# print('After calling loop')

# tasks = [request() for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
#
# # task = asyncio.ensure_future(coroutine)
# # task.add_done_callback(callback)
# # print('Task:', task)
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(task)
# print('Task:', task)


# ========================
# 多任务协程


import asyncio
import requests


async def request():
    url = 'http://127.0.0.1:5000/api'
    status = requests.get(url)
    return status


tasks = [asyncio.ensure_future(request()) for _ in range(5)]
print('Tasks:', tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

for task in tasks:
    print('Task Result:', task.result())




