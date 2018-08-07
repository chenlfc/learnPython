# -*- coding: utf-8 -*-
# create by o.c. 2018/8/6
# file name : people.py

import pygame


class People():
    """创建一个小人的类"""

    def __init__(self, settings, screen):

        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load(settings.people_image)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        # 设置小人的移动开关
        self.move_left = False
        self.move_right = False

    def draw_people(self):
        """在指定位置绘制小人"""
        self.screen.blit(self.image, self.rect)

    def update_people(self):
        """更新小人的位置"""
        if self.move_left and self.rect.left > 0:
            self.center -= self.settings.people_speed_factor
        elif self.move_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.people_speed_factor
        self.rect.centerx = self.center
