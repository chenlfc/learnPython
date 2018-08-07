# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/27
# from _for_ex import pt_title

# pt_title('EX 12 - 1')

# import sys
import pygame

import ex12_1_flower as fl
import ex12_1_settings as se
import ex12_1_functions as fu

from pygame.sprite import Group


def run_game():
    pygame.init()  # 创建一个屏幕对象
    setting = se.Settings()
    screen = pygame.display.set_mode((setting.s_width, setting.s_height))

    icon = pygame.image.load(setting.icon)
    pygame.display.set_icon(icon)
    pygame.display.set_caption(setting.caption)
    flower = fl.Flower(setting, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    while True:
        fu.check_events(setting, screen, flower, bullets)
        flower.update_moving()
        bullets.update()

        fu.update_bullets(bullets)
        fu.update_screen(setting, screen, flower, bullets)


run_game()
