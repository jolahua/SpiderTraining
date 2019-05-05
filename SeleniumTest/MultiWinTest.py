#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: Jola
# datetime:2019/5/2 21:47
# software-version: python 3.6


import time

from selenium import webdriver
from tools import chromedriver_path


def main():
    driver = webdriver.Chrome()
    # driver = webdriver.Chrome(executable_path=chromedriver_path)
    # 打开浏览器，窗口最大化
    driver.maximize_window()
    driver.get("http://baidu.com")
    # 停留两秒后打开搜狗搜索
    time.sleep(0.5)
    JS1 = 'window.open("https://www.sogou.com");'
    driver.execute_script(JS1)
    # 停留两秒后打开有道翻译
    time.sleep(0.5)
    JS2 = 'window.open("https://fanyi.youdao.com/");'
    driver.execute_script(JS2)
    time.sleep(10)
    # 退出
    # driver.quit()


if __name__ == '__main__':
    main()


