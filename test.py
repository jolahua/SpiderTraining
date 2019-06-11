#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author: Jola
# @Time: 2019/5/6 17:17


def main(text=''):

    if text == '':
        print('请复制您的headers到此处，输入【:q】结束输入: ')
        for line in iter(input, ':q'):
            text += line + '\n'

    text = text.replace(' ', '').replace('\'', '\"')
    result = []
    text = text.replace('{', '').replace('}', '').replace(':q', '')
    for each in text.split('\n'):
        if each == '':
            continue
        tag, attr = each.split(':')[0], ''.join(each.split(':')[1:])
        result.append(': '.join(['\'' + e + '\'' for e in [tag, attr]]) + ',')
    result[-1] = result[-1].rstrip(',')
    return '\n'.join(result)


if __name__ == '__main__':
    text = '''
     Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: max-age=0
Connection: keep-alive
Cookie: bid=bykfTb_1r1g; ll="118282"; _vwo_uuid_v2=D8A4ECC4BC6BDD419E874EA99E608128F|e6d5f936f2bcb3847f550d782c23c94b; __yadk_uid=QoabSrx4NuTood6WHJ2KUp0tMlQI8DXh; _ga=GA1.2.1103580898.1556506102; trc_cookie_storage=taboola%2520global%253Auser-id%3Df3ebb457-4cb8-47cc-94a8-6f29ba0745ee-tuct3a5f2d3; __utmc=30149280; __utmc=223695111; __utmz=223695111.1559208729.3.2.utmcsr=m.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/movie/comment/1784342194; __utmz=30149280.1559267643.4.3.utmcsr=json.cn|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1559637524%2C%22https%3A%2F%2Fm.douban.com%2Fmovie%2Fcomment%2F1784342194%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.1103580898.1556506102.1559267643.1559637524.5; __utmb=30149280.0.10.1559637524; __utma=223695111.1103580898.1556506102.1559208729.1559637524.4; __utmb=223695111.0.10.1559637524; ap_v=0,6.0; _pk_id.100001.4cf6=fd3ccea7b7f68627.1559118448.4.1559637527.1559208891.
Host: movie.douban.com
Referer: https://movie.douban.com/subject/26928226/
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36
        '''
    print(main(text))
    # print(any([True for i in ['）', '（', '(', ')'] if i in '2(OCT),3(其他),null（未']))
