#!/usr/bin/env python
# -*- coding: utf-8 -*-




"""
获取豆瓣电影中的电影资源
豆瓣电影url地址：https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0
分析：
    1. 该页面中的的电影资源信息都是通过ajax异步加载进行刷新出来的
    2. 在F12下的network中过滤XHR(XMLHTTPRESPONSE)请求，可以查看到真正的异步的请求地址如下
        https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=20
    3. 正在的请求地址中，type为类型，tag为标签（热门、经典、最新、爱情、科幻等等），sort为排序，page_limit为每一个的条数，page_start为开始的条数下标
    4. 获取tag类型的url地址为： https://movie.douban.com/j/search_tags?type=movie&source=
"""


import urllib.request
from urllib import parse
import requests
import json
import time
import threading
import pymongo




def urllib_open(url):
    """
    公共的处理代码
    """
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    req = requests.get(url=url, headers=header)
    # req = urllib.request.Request(url=url, headers=header)
    # res = urllib.request.urlopen(req)
    #return res.read().decode('utf-8')
    return req.text


def get_movie_tag(url):
    """
    获取电影的分类tag
    """
    tag_res = urllib_open(url)
    # 返回的tag_res的结果为'{"tags":["热门","最新","经典","可播放","豆瓣高分","冷门佳片","华语","欧美","韩国","日本","动作","喜剧","爱情","科幻","悬疑","恐怖","成长"]}'
    # 其结果为一个字符串类型的数据，需要将之转化为字典类型的
    result = json.loads(tag_res)
    content = result['tags']
    return content


def get_movies(movies_url, db):
    # movies_url中指定电影类型的参数是tag=热门或者最新等等
    # db 是mongo的对象，可以操作mongo数据库
    movies_res = urllib_open(movies_url)
    res = json.loads(movies_res)
    result = res['subjects']
    for res in result:
        db.movies2.insert_one({
            'm_name': res['title'],
            'm_rate': res['rate']
        })
        print('标题:%s，评分：%s' % (res['title'], res['rate']))


def main():

    # 设置数据库的访问

    client = pymongo.MongoClient('localhost', 27017)
    db = client.reports
    db.authenticate("admin", "admin")
    collection = db.movies2
    tag_url = 'https://movie.douban.com/j/search_tags?type=movie&source='
    movies_url = 'https://movie.douban.com/j/search_subjects?type=movie&%s&sort=recommend&page_limit=20&page_start=0'
    tag_content = get_movie_tag(tag_url)
    threading_list = []
    result_list = []
    for tag in tag_content:
        search_url = movies_url
        data = {'tag': tag}
        search_tag = parse.urlencode(data)
        result_list.append(search_url % (search_tag,))

    for url in result_list:
        t = threading.Thread(target=get_movies, args=(url, db))
        threading_list.append(t)

    for thread in threading_list:
        thread.start()
        # thread.join()


if __name__ == '__main__':
    print(time.clock())
    main()
    print(time.clock())