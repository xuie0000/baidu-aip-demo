#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author Jie Xu
@date 2018-12-21
"""

from aip import AipImageClassify

""" 你的 APPID AK SK """
APP_ID = '15228369'
API_KEY = '3X0DrqNFMshRMbWsSfCBv3ek'
SECRET_KEY = 'XCzazG2h1qu4v5drwutPDk9fvfIpX3s5'

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(file_path):
    """ 读取图片 """
    with open(file_path, 'rb') as fp:
        return fp.read()


def main():
    image = get_file_content('baidu_cat.jpeg')

    """ 调用通用物体识别 """
    s = client.advancedGeneral(image)

    # """ 如果有可选参数 """
    # options = {}
    # options["baike_num"] = 5
    #
    # """ 带参数调用通用物体识别 """
    # s = client.advancedGeneral(image, options)

    print(s)


if __name__ == '__main__':
    main()
