# -*- coding: utf-8 -*-
# create by o.c. 2018/8/3
# file name : settings.py


class Settings():
    """对于程序的一些设置"""

    def __init__(self):
        # 对屏幕的设置参数
        self.screen_width = 800
        self.screen_height = 450
        self.screen_caption = '--- The Rains ---'
        bg_color = 2
        self.screen_bg_color = (bg_color, bg_color, bg_color)

        # 对雨滴的设置参数
        self.rain_width = 1
        self.rain_max_width = 2
        self.rain_max_height = 60
        self.rain_min_height = 5
        self.rain_speed_factor = 1
        self.rain_max_color = bg_color + 50
        self.rain_min_color = bg_color + 3

        self.rain_max_number = 1000
        self.rain_min_number = 500
        self.rain_number = 800

        # 对星星的设置参数
        self.star_min_scale = 3
        self.star_max_scale = 10
        self.star_min_color = bg_color + 3
        self.star_max_color = bg_color + 40

        self.star_x = 1
        self.star_y = 1
