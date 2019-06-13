#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author: Jola
# @Time: 2019/6/11 16:52


# from cairosvg import svg2png
import pygame  # pip install pygame
import winsound


# 貌似只能播放单声道音乐，可能是pygame模块限制
def playMusic(filename, loops=0, start=0.0, value=0.5):
    """
    :param filename: 文件名
    :param loops: 循环次数
    :param start: 从多少秒开始播放
    :param value: 设置播放的音量，音量value的范围为0.0到1.0
    :return:
    """
    flag = False  # 是否播放过
    pygame.mixer.init()  # 音乐模块初始化
    while 1:
        if flag == 0:
            pygame.mixer.music.load(filename)
            # pygame.mixer.music.play(loops=0, start=0.0) loops和start分别代表重复的次数和开始播放的位置。
            pygame.mixer.music.play(loops=loops, start=start)
            pygame.mixer.music.set_volume(value)  # 来设置播放的音量，音量value的范围为0.0到1.0。
        if pygame.mixer.music.get_busy() == True:
            flag = True
        else:
            if flag:
                pygame.mixer.music.stop()  # 停止播放
                break


def svg_test():
    svg_code = """
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="10"/>
            <line x1="12" y1="8" x2="12" y2="12"/>
            <line x1="12" y1="16" x2="12" y2="16"/>
        </svg>
    """

    # svg2png(bytestring=svg_code, write_to='output.png')


if __name__ == '__main__':

    import os

    file = r'E:\Jola\crawler\SpiderTraining\1.mp3'
    # winsound.PlaySound(file, winsound.SND_ASYNC)

    os.system("start " + file)

    # playMusic(file)

    # import os
    # os.startfile(file)



