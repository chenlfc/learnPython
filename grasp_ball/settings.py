# -*- coding: utf-8 -*-
# create by o.c. 2018/8/6
# file name : settings.py


class Settings():
    """一些程序的设置"""

    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.screen_caption = '--- Grasp Ball ---'
        self.bg_color = (230, 230, 230)

        self.people_speed_factor = 2
        self.people_image = './images/people.jpg'

        self.ball_radius = 10
        self.ball_mix_color = 200
        self.ball_speed_factor = 1

        self.get_ball = 0
        self.lose_ball = 0
        self.totle_ball = 0

        self.people_limit = 3
