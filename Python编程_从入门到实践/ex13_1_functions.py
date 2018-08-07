# -*- coding: utf-8 -*-
# create by o.c. 2018/8/1
# file name : ex13_1_functions.py

import sys
from random import randint
import pygame

from ex13_1_star import Star


def create_star(settings, screen, stars, star_number, row_number):
    """创建一颗星星"""
    # 计算并设置星星的x坐标位置
    star = Star(settings, screen)
    star_width = star.rect.width
    star_height = star.rect.height

    star.x = star_width + 2 * star_width * star_number + randint(-10, 10)
    star.rect.x = star.x

    star.y = star_height + 2 * star_height * row_number + randint(-10, 10)
    star.rect.y = star.y

    stars.add(star)


def get_rows(settings, star_height):
    """计算屏幕总共能放几行星星"""
    # 计算屏幕能放星星的总高度，上下叶各留一行星星的空间
    avilable_space_y = settings.screen_height - star_height
    number_rows = int(avilable_space_y / (2 * star_height))
    return number_rows


def get_number_star_x(settings, star_width):
    """计算一行能放的星星的数量"""
    # 计算屏幕能够摆放星星的总宽度是多少，两边各留一颗星星的空间
    avilable_space_x = settings.screen_width - star_width
    # 计算星星之间的总空隙
    # number_star_x = int(avilable_space_x / (2 * star_width))
    number_star_x = int(avilable_space_x / (2 * star_width))
    return number_star_x


def create_stars(settings, screen, stars):
    """创建星星群"""
    star = Star(settings, screen)
    number_star_x = get_number_star_x(settings, star.rect.width)
    number_rows = get_rows(settings, star.rect.height)
    # 创建满屏的星星
    for star_row in range(number_rows):
        # 创建一行星星
        for star_number in range(number_star_x):
            # 创建一颗星星
            create_star(settings, screen, stars, star_number, star_row)


def check_events():
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()


def update_screen(settings, screen, stars):
    """更新屏幕"""
    screen.fill(settings.b_color)

    stars.draw(screen)

    # 让最近绘制的内容屏幕可见
    pygame.display.flip()
