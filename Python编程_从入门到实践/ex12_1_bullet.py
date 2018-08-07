# -*- coding: utf-8 -*-
# create by o.c. 2018/7/30
# file name : ex12_1_bullet.py

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """一个对发射的子弹进行管理的类"""

    def __init__(self, settings, screen, flower):
        """在花所处的位置创建一个子弹对象"""
        super().__init__()
        self.screen = screen

        # 在(0, 0)处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, settings.bullet_width,
                                settings.bullet_height)
        self.rect.centerx = flower.rect.left
        self.rect.centery = flower.rect.centery

        # 储存用小数表示的子弹位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor

        # 尝试绘制一个圆形, pos是圆心位置的坐标
        self.circle_x = flower.rect.left
        self.circle_y = flower.rect.centery
        self.circle_pos = (self.circle_x, self.circle_y)

    def update_bullet(self):
        """向左移动子弹"""
        # 更新表示子弹位置的小数值
        self.x -= self.speed_factor
        # 更新表示子弹的真实位置
        self.rect.x = self.x
        self.circle_x -= self.speed_factor
        self.circle_pos = (self.circle_x, self.circle_y)

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.draw.circle(self.screen, self.color, self.circle_pos, 10, 5)

