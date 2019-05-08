#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author: Jola
# @Time: 2019/5/6 17:17


import re
import time
import requests


def main():

    t = '0(眼底照相),1(荧光造影),2(OCT),3(其他),null（未标注）'.replace(',', '，').replace('(', '（').replace(')', '）')
    pattern = '(.*)（(.*)）'
    for each in t.split('，'):
        res = re.match(re.compile(pattern), each)
        print(res.groups())


if __name__ == '__main__':
    # main()
    print(any([True for i in ['）', '（', '(', ')'] if i in '2(OCT),3(其他),null（未']))
