# -*- coding: utf-8 -*-
# create by o.c. 2018/7/27
# file name : ex12-1_flower.py

import pygame


class Flower():
    def __init__(self, fl_settings, screen):
        self.screen = screen
        self.settings = fl_settings
        self.image = pygame.image.load(fl_settings.flower_image)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        # 为了使用浮点数，所以使用center代替centerx和centery
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # 设置移动开关
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def update_moving(self):
        """根据移动开关移动flower对象"""
        # 使用centerx 和centery 代替 rect.centerx 和rect.centery
        # 检测边界是否超过屏幕边界，使用screen_rect的相关属性
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.settings.flower_speed_factor
        elif self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.settings.flower_speed_factor
        elif self.moving_up and self.rect.top > 0:
            self.centery -= self.settings.flower_speed_factor
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.settings.flower_speed_factor
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        self.screen.blit(self.image, self.rect)
