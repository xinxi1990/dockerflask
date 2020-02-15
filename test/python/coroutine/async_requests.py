
import asyncio
import requests
import time
import aiohttp

start = time.time()

# async def request():
#     url = 'http://127.0.0.1:5000/api'
#     print('Waiting for', url)
#     response = requests.get(url)
#     print('Get response from', url, 'Result:', response.text)

async def get(url):
    return requests.get(url)


async def request():
    url = 'http://127.0.0.1:5000/api'
    print('Waiting for', url)
    response = await get(url)
    print('Get response from', url, 'Result:', response.text)


async def aiohttp_get():
    url = 'http://127.0.0.1:5000/api'
    print('Waiting for', url)
    session = aiohttp.ClientSession()
    response = await session.get(url)
    result = await response.text()
    print('Get response from', url)
    session.close()
    return result


tasks = [asyncio.ensure_future(aiohttp_get()) for _ in range(100)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))