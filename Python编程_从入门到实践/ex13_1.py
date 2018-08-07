# -*- coding: utf-8 -*-
# create by o.c. 2018/8/1
# file name : ex13_1.py

import pygame
from pygame.sprite import Group

from ex13_1_setting import Settings
import ex13_1_functions as fu


def run_star_game():
    """程序核心"""
    pygame.init()

    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width,
                                      settings.screen_height))
    pygame.display.set_caption(settings.caption)

    # 创建一群星星
    stars = Group()
    fu.create_stars(settings, screen, stars)

    # 开始程序的主循环
    while True:
        # 响应按键和鼠标事件
        fu.check_events()

        # 每次循环时都重绘屏幕
        fu.update_screen(settings, screen, stars)


run_star_game()
