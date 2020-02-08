#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
生成用户反馈词云
"""

from wordcloud import WordCloud
import PIL.Image as image
import numpy as  np
import jieba
import re # 正则表达式库
import collections # 词频统计库
import numpy as np # numpy数据处理库
import jieba # 结巴分词
import wordcloud # 词云展示库
from PIL import Image # 图像处理库
import matplotlib.pyplot as plt # 图像展示库


def cut_text(file='feedback.text'):
    with open(file,mode='r') as r:
        result = r.read()

    word_list = jieba.cut(result)

    seg_list_exact = (' '.join(word_list))

    font_path = '/System/Library/fonts/PingFang.ttc'
    # 生成对象
    wc = WordCloud(collocations=False, font_path=font_path, width=1400, height=1400, margin=2).generate(text=seg_list_exact)

    # 显示词云
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.show()

    # 保存文件
    wc.to_file('wordcloud.png')


    # object_list = []
    # remove_words = [u'的', u'，', u'和', u'是', u'随着', u'对于', u'对', u'等', u'能', u'都', u'。', u' ', u'、', u'中', u'在', u'了',
    #                 u'通常', u'如果', u'我们', u'需要']  # 自定义去除词库

    # for word in seg_list_exact:  # 循环读出每个分词
    #     if word not in remove_words:  # 如果不在去除词库中
    #         object_list.append(word)  # 分词追加到列表
    #
    # # 词频统计
    # word_counts = collections.Counter(object_list)  # 对分词做词频统计
    # word_counts_top10 = word_counts.most_common(10)  # 获取前10最高频的词
    # print(word_counts_top10)  # 输出检查
    #
    # # 词频展示
    # mask = np.array(Image.open('wordcloud.jpg'))  # 定义词频背景
    # wc = wordcloud.WordCloud(
    #     # font_path='C:/Windows/Fonts/simhei.ttf',  # 设置字体格式
    #     mask=mask,  # 设置背景图
    #     max_words=200,  # 最多显示词数
    #     max_font_size=100  # 字体最大值
    # )
    #
    # wc.generate_from_frequencies(word_counts)  # 从字典生成词云
    # image_colors = wordcloud.ImageColorGenerator(mask)  # 从背景图建立颜色方案
    # wc.recolor(color_func=image_colors)  # 将词云颜色设置为背景图方案
    # plt.imshow(wc)  # 显示词云
    # plt.axis('off')  # 关闭坐标轴
    # plt.show()  # 显示图像



cut_text()
