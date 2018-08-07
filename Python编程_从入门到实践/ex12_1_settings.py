# -*- coding: utf-8 -*-
# create by o.c. 2018/7/27
# file name : ex12_1_settings.py


class Settings():
    def __init__(self):
        # 设置屏幕相关参数
        self.caption = ':: My Flower Screen ::'
        self.icon = 'E:/learnPython/_images/flower.bmp'
        self.s_width = 800
        self.s_height = 600
        self.bg_color = (0, 0, 255)
        # 设置flower相关的参数
        self.flower_image = 'E:/learnPython/_images/flower.bmp'
        self.flower_speed_factor = 1.0
        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (255, 0, 255)
        self.bullet_allower = 5
