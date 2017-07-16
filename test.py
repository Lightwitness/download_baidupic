#!/usr/bin/env python
# encoding: utf-8
"""
@version: python2.7
@author: Lightwitness
@contact: 498969498@qq.com
@software: PyCharm
@file: test.py
@time: 2017/7/15 13:52
"""

import requests
from lxml import etree
import os
import urllib


def pic():
    all_url = 'http://image.baidu.com/'
    start_html = requests.get(all_url, timeout=10)
    selector = etree.HTML(start_html.text)

    selectPic = selector.xpath('//*[@id="wrapper_content_box"]/div[2]/div[1]/div/div/a/div[4]/img/@src')

    for picture in selectPic:
        u = urllib.urlopen(picture)
        data = u.read()
        pictureName = picture.split('_')[0]
        with open('picture/' + pictureName.split('/')[-1], 'wb') as f:
            print '正在保存:' + pictureName.split('/')[-1]
            f.write(data)  # 保存当前页的图片数据



if __name__ == '__main__':
     pic()