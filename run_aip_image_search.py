#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author Jie Xu
@date 2018-12-21
"""

from aip import AipImageSearch

""" 你的 APPID AK SK """
APP_ID = '15232720'
API_KEY = 'E77Oz5vYKkRdn6VKVYKhpjGO'
SECRET_KEY = '28QDYwVhIrZS9bvtnDu6ufdvexDeyCoy'

client = AipImageSearch(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(file_path):
    """ 读取图片 """
    with open(file_path, 'rb') as fp:
        return fp.read()


def main():
    """http://ai.baidu.com/docs#/ImageSearch-Python-SDK/top"""
    image = get_file_content('baidu_cat.jpeg')

    """ 调用相同图检索—入库, 图片参数为本地图片 """
    s = client.similarSearch(image)

    print(s)

    # """ 如果有可选参数 """
    # options = {}
    # options["tags"] = "100,11"
    # options["tag_logic"] = "0"
    # options["pn"] = "100"
    # options["rn"] = "250"
    #
    # """ 带参数调用相似图检索—检索, 图片参数为本地图片 """
    # client.similarSearch(image, options)
    #
    # url = "http//www.x.com/sample.jpg"
    #
    # """ 调用相似图检索—检索, 图片参数为远程url图片 """
    # client.similarSearchUrl(url);
    #
    # """ 如果有可选参数 """
    # options = {}
    # options["tags"] = "100,11"
    # options["tag_logic"] = "0"
    # options["pn"] = "100"
    # options["rn"] = "250"
    #
    # """ 带参数调用相似图检索—检索, 图片参数为远程url图片 """
    # client.similarSearchUrl(url, options)


if __name__ == "__main__":
    main()
