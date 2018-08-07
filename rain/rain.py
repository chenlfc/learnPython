# -*- coding: utf-8 -*-
# create by o.c. 2018/8/3
# file name : rain.py

from random import randint
import pygame
from pygame.sprite import Sprite


class Rain(Sprite):
    """定义一滴雨对象的类"""

    def __init__(self, settings, screen):
        """对雨滴的设置并初始化"""
        super().__init__()

        self.settings = settings
        self.screen = screen


        self.rain_width = randint(settings.rain_width, settings.rain_max_width)
        self.rain_height = randint(settings.rain_min_height,
                                   settings.rain_max_height)

        self.rect = pygame.Rect(0, 0, self.rain_width, self.rain_height)
        self.r_x = 3
        self.r_y = randint(settings.rain_max_height * -1,
                           settings.rain_max_height)

        self.rect.x = float(self.r_x)
        self.rect.y = float(self.r_y)

        rgb_color = randint(settings.rain_min_color, settings.rain_max_color)
        self.color = (rgb_color, rgb_color, rgb_color)

    def update_rain(self):
        """让雨滴落下"""
        self.r_y += randint(self.settings.rain_speed_factor,
                            self.settings.rain_speed_factor * 2)
        # self.r_y += randint(self.settings.rain_speed_factor,
        #                     int(self.settings.rain_max_height / 6))
        # if self.r_y > self.settings.screen_height:
        #     self.r_y = 0
        self.rect.y = float(self.r_y)

    def draw_rain(self):
        """在屏幕上绘制雨滴"""
        pygame.draw.rect(self.screen, self.color, self.rect)
