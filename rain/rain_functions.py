# -*- coding: utf-8 -*-
# create by o.c. 2018/8/3
# file name : rain_functions.py

from random import randint
import sys
import pygame

from rain import Rain
from star import Star


def get_star_row(settings):
    """计算屏幕高度内放几行星星"""
    screen_height_space = settings.screen_height - 3 * settings.star_max_scale
    row_star = int(screen_height_space / (1 * settings.star_max_scale))
    return row_star


def get_number_star(settings):
    """计算屏幕宽度内的星星数量"""
    screen_width_space = settings.screen_width - 3 * settings.star_max_scale
    number_star = int(screen_width_space / (1 * settings.star_max_scale))
    return number_star


def create_star(settings, screen, stars, star_number, star_row):
    """创建星星"""
    star = Star(settings, screen)
    star.p_x = star_number * settings.star_max_scale + randint(
        1, settings.star_max_scale)
    star.p_y = star_row * settings.star_max_scale + randint(
        1, settings.star_max_scale)

    star.update_point_list()
    stars.add(star)


def create_stars(settings, screen, stars):
    """创建星星群"""
    number_star = get_number_star(settings)
    row_star = get_star_row(settings)

    for star_row in range(row_star):
        for star_number in range(number_star):
            create_star(settings, screen, stars, star_number, star_row)


def get_number_rain(settings):
    """计算屏幕宽度内雨滴的数量"""
    screen_width_space = settings.screen_width - 3 * settings.rain_width
    number_rain = int(screen_width_space / (1 * settings.rain_width))

    return number_rain


def create_rain(settings, screen, rains, rain_number):
    """创建雨滴"""
    rain = Rain(settings, screen)
    r_width = settings.rain_width
    r_height = settings.rain_max_height

    rain.r_x = r_width + int((rain_number * r_width * randint(1, 3)))
    rain.r_y = r_height + r_height * randint(-10, r_height)
    rain.rect.x = rain.r_x
    rain.rect.y = rain.r_y

    rains.add(rain)


def create_rains(settings, screen, rains):
    """创建雨滴群"""
    number_rain = get_number_rain(settings)

    for rain_number in range(number_rain):
        create_rain(settings, screen, rains, rain_number)


def check_event(settings, screen, stars):
    """响应鼠标与键盘"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_UP:
                if settings.rain_speed_factor > 0:
                    settings.rain_speed_factor -= 1
            elif event.key == pygame.K_DOWN:
                if settings.rain_speed_factor < 10:
                    settings.rain_speed_factor += 1
            elif event.key == pygame.K_LEFT:
                if settings.rain_number > settings.rain_min_number:
                    settings.rain_number -= 20
            elif event.key == pygame.K_RIGHT:
                if settings.rain_number < settings.rain_max_number:
                    settings.rain_number += 20
            elif event.key == pygame.K_F5:
                update_stars(settings, screen, stars)


def update_screen(settings, screen, rains, stars):
    """每次循环都刷新屏幕"""
    screen.fill(settings.screen_bg_color)

    for star in stars.sprites():
        star.draw_star()

    for rain in rains.sprites():
        rain.draw_rain()
        rain.update_rain()

    pygame.display.flip()


def update_rains(settings, screen, rains):
    """另一种控制雨滴落到屏幕外的操作方式"""
    # pygame.sprite.groupcollide(rains, stars, True, False)
    rains.update()
    settings.screen_caption = (
        '--- The Rains --- :: RAIN SPEED FACTOR = ' + str(
            settings.rain_speed_factor) + ' :: RAIN NUMBER = ' + str(
                settings.rain_number) + ' :: RAIN NOW NUMBER = ' + str(
                    rains.__len__())).title()
    # print('+', rains.__len__(), end=' ')
    for rain in rains.copy():
        if rain.rect.top > settings.screen_height:
            rains.remove(rain)
            if rains.__len__() < settings.rain_number:
                # print('-', rains.__len__(), end=' ')
                create_rains(settings, screen, rains)


def update_stars(settings, screen, stars):
    """重新绘制所有的星星"""
    stars.update()
    for star in stars.copy():
        stars.remove(star)
    create_stars(settings, screen, stars)
