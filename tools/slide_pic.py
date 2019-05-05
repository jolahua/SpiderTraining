#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author: Jola
# @Time: 2019/5/5 17:13


from PIL import Image


def main():
    img1 = Image.open('1.jpg')
    print(img1.size)
    for w, h in zip(*[range(i) for i in img1.size]):
        print(img1.getpixel((w, h)))
    # img1 = img1.convert('L')
    # img1.show()


if __name__ == '__main__':
    main()


