# -*- coding: utf-8 -*-
# create by o.c. 2018/7/27
# file name : ex12_1_function.py

import sys
import pygame
from ex12_1_bullet import Bullet


def check_events(settings, screen, flower, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # 检查按键
            check_key_down(event, settings, screen, flower, bullets)
        elif event.type == pygame.KEYUP:  # 检查松开按键
            check_key_up(event, flower)


def check_key_down(event, settings, screen, flower, bullets):
    """检查按键"""
    if event.key == pygame.K_RIGHT:
        # 向右移动花朵
        flower.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 向左移动花朵
        flower.moving_left = True
    elif event.key == pygame.K_UP:
        # 向上移动花朵
        flower.moving_up = True
    elif event.key == pygame.K_DOWN:
        # 向下移动花朵
        flower.moving_down = True
    elif event.key == pygame.K_SPACE:
        # 按空格时发射子弹
        fire_bullet(settings, screen, flower, bullets)


def check_key_up(event, flower):
    """检查松开"""
    if event.key == pygame.K_RIGHT:
        # 向右移动花朵
        flower.moving_right = False
    elif event.key == pygame.K_LEFT:
        # 向左移动花朵
        flower.moving_left = False
    elif event.key == pygame.K_UP:
        # 向上移动花朵
        flower.moving_up = False
    elif event.key == pygame.K_DOWN:
        # 向下移动花朵
        flower.moving_down = False


def fire_bullet(settings, screen, flower, bullets):
    """如果如果还没有到达子弹上限，就发射一颗子弹"""
    if len(bullets) < settings.bullet_allower:
        new_bullet = Bullet(settings, screen, flower)
        bullets.add(new_bullet)


def update_screen(setting, screen, flower, bullets):
    screen.fill(setting.bg_color)
    flower.blitme()
    # 重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        bullet.update_bullet()

    pygame.display.flip()


def update_bullets(bullets):
    """更新子弹的位置， 并删除已消失的子弹"""
    bullets.update()
    # 删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.left <= 0:
            bullets.remove(bullet)
