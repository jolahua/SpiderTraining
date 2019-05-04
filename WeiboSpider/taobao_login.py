#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author: Jola
# @Time: 2019/4/29 15:35


"""
使用教程：
1.下载chrome浏览器:https://www.google.com/chrome/
2.查看chrome浏览器的版本号，下载对应版本号的chromedriver驱动:http://chromedriver.storage.googleapis.com/index.html
3.填写chromedriver的绝对路径
4.执行命令pip install selenium
5.打开https://account.weibo.com/set/bindsns/bindtaobao并通过微博绑定淘宝账号密码
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from tools import weibo_username, weibo_password, chromedriver_path, pwd, user


# 定义一个taobao类
class TBInfo(object):

    # 对象初始化
    def __init__(self):
        url = 'https://login.taobao.com/member/login.jhtml'
        self.url = url

        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})  # 不加载图片,加快访问速度
        options.add_experimental_option('excludeSwitches',
                                        ['enable-automation'])  # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium

        self.browser = webdriver.Chrome(executable_path=chromedriver_path, options=options)
        self.wait = WebDriverWait(self.browser, 10)  # 超时时长为10s

    # 登录淘宝
    def login(self):
        # 打开网页
        self.browser.get(self.url)

        # 等待 密码登录选项 出现
        password_login = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.qrcode-login > .login-links > .forget-pwd')))
        password_login.click()

        # 等待 微博登录选项 出现
        weibo_login = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.weibo-login')))
        weibo_login.click()

        # 等待 微博账号 出现
        weibo_user = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.username > .W_input')))
        weibo_user.send_keys(weibo_username)

        # 等待 微博密码 出现
        weibo_pwd = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.password > .W_input')))
        weibo_pwd.send_keys(weibo_password)

        # 等待 登录按钮 出现
        submit = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn_tip > a > span')))
        submit.click()

        # 直到获取到淘宝会员昵称才能确定是登录成功
        tb_name_css = '.site-nav-bd > ul.site-nav-bd-l > li#J_SiteNavLogin > div.site-nav-menu-hd ' \
                      '> div.site-nav-user > a.site-nav-login-info-nick '
        # tb_name_css = '#pl_login_logged > div > div:nth-child(7) > div:nth-child(1) > a > span'
        taobao_name = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, tb_name_css)))
        # 输出淘宝昵称
        print(taobao_name.text)

    def login_main(self):
        self.browser.get(self.url)

        # 等待 密码登录选项 出现
        password_login = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.qrcode-login > .login-links > .forget-pwd')))
        password_login.click()

        user_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#TPL_username_1')))
        user_input.send_keys(user)

        pwd_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#TPL_password_1')))
        pwd_input.send_keys(pwd)

        submit = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#J_SubmitStatic')))
        submit.click()


if __name__ == "__main__":

    a = TBInfo()
    a.login()  # 登录
    # a.login_main()  # 登录


