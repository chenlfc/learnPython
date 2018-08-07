# -*- coding: utf-8 -*-
# create by o.c. 2018/8/6
# file name : grasp_ball_functions.py

from random import randint
import sys
from time import sleep

import pygame
from ball import Ball

# from people import People


def create_ball(settings, screen, balls):
    """创建一个球体集合"""
    ball = Ball(settings, screen)
    ball_x = randint(settings.ball_radius,
                     settings.screen_width - settings.ball_radius)
    ball.ball_centerx = ball_x
    balls.add(ball)


# def create_people(settings, screen, peoples):
#     """创建小人集合"""
#     people = People(settings, screen)
#     peoples.add(people)


def check_events(people):
    """响应鼠标和键盘"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, people)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, people)


def check_keyup_events(event, people):
    """响应按键弹起"""
    if event.key == pygame.K_LEFT:
        people.move_left = False
    elif event.key == pygame.K_RIGHT:
        people.move_right = False


def check_keydown_events(event, people):
    """响应按键按下去"""
    if event.key == pygame.K_LEFT:
        people.move_left = True
    elif event.key == pygame.K_RIGHT:
        people.move_right = True
    elif event.key == pygame.K_q:
        sys.exit()


def update_screen(settings, screen, people, balls):
    """更新屏幕图形"""
    screen.fill(settings.bg_color)
    people.update_people()
    people.draw_people()

    for ball in balls.sprites():
        ball.draw_ball()

    pygame.display.flip()


def update_ball(settings, stats, screen, people, balls):
    """更新球的位置，当遇到屏幕边缘或小人时消失并创建一个新的小球"""
    if stats.people_left > 0:
        if pygame.sprite.spritecollide(people, balls, True):
            create_ball(settings, screen, balls)
            settings.get_ball += 1
            settings.totle_ball += 1

        for ball in balls.sprites():
            ball.update_ball()
            # print('-', collisions)
            if ball.ball_centery >= settings.screen_height:
                ball.ball_centery = settings.ball_radius
                balls.remove(ball)
                people.rect.centerx = screen.get_rect().centerx

                create_ball(settings, screen, balls)

                settings.lose_ball += 1
                settings.totle_ball += 1
                stats.people_left -= 1

        pygame.display.set_caption(
            settings.screen_caption + " :: Get Ball (" +
            str(settings.get_ball) + ") :: Lose Ball (" +
            str(settings.lose_ball) + ") :: Total Ball (" +
            str(settings.totle_ball) + ")")
    else:
        stats.game_active = False
