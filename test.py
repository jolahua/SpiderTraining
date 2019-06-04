#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author: Jola
# @Time: 2019/5/6 17:17


import re
import time
import requests


def main(text=''):

    if text == '':
        print('请复制您的headers到此处，输入【:q】结束输入: ')
        for line in iter(input, ':q'):
            text += line.replace('\'', '\"') + '\n'
    result = []
    text = text.replace('{', '').replace('}', '').replace(':q', '')
    for each in text.split('\n'):
        if each == '':
            continue
        tag, attr = each.split(':')[0], ''.join(each.split(':')[1:])
        result.append(': '.join(['\'' + e.replace('', '') + '\'' for e in [tag, attr]]) + ',')
    return '\n'.join(result)


if __name__ == '__main__':
    print(main())
    # print(any([True for i in ['）', '（', '(', ')'] if i in '2(OCT),3(其他),null（未']))
