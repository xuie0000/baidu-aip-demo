#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author Jie Xu
@date 2018-12-21
"""
import json

from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '15132616'
API_KEY = 'MR7kO5GMvCjkypoUvMlpqQ3g'
SECRET_KEY = 'QWEGTkcgxEkXCHbYGQHrQwO4Y8jM3tRx'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

PUNC_TOBE_REP = "!?,.:;“”()"
PUNC_AFBE_REP = "！？，。：；\"\"（）"
RM_HOLE_FLAG = True


def custom_rep(s):
    if len(PUNC_TOBE_REP) != len(PUNC_AFBE_REP):
        raise ValueError(" | What the fuck did you modified...")
    for i in range(len(PUNC_TOBE_REP)):
        s = s.replace(PUNC_TOBE_REP[i], PUNC_AFBE_REP[i])
    if RM_HOLE_FLAG is True:
        s = s.replace("\n", "")
        s = s.replace(" ", "")
    s = s.replace("一一", " -- ")
    s = s.replace("。。。。。", "...")
    s = s.replace("。。。。", "...")
    # print (" | Replace completed...")
    return s


""" 读取图片 """


def get_file_content(file_path):
    with open(file_path, 'rb') as fp:
        return fp.read()


def main():
    """说明文档：http://ai.baidu.com/docs#/OCR-Python-SDK/top"""
    image = get_file_content('./example.jpg')

    """ 调用通用文字识别（高精度版） """
    s = client.basicAccurate(image)

    # """ 如果有可选参数 """
    # options = {}
    # options["detect_direction"] = "true"
    # options["probability"] = "true"
    #
    # """ 带参数调用通用文字识别（高精度版） """
    # client.basicAccurate(image, options)

    if s != "":
        print(s)
        data_string = json.dumps(s, ensure_ascii=False)
        print("object to json string:" + data_string)
        # print("json string to object:" + json.loads(custom_rep(data_string)))
    else:
        print(" | No any characters...")
    # print (" | All done!")


if __name__ == "__main__":
    main()
