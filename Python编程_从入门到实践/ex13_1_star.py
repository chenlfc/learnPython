# -*- coding: utf-8 -*-
# create by o.c. 2018/8/1
# file name : ex13_1_setting.py

from random import randint
import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """创建一颗星星的类"""

    def __init__(self, settings, screen):
        """设置星星的相关属性"""
        super().__init__()
        self.screen = screen
        self.settings = settings

        # 加载星星的图像，并设置其rect属性
        self.images = (pygame.image.load('../_images/star_yellow.bmp'),
                       pygame.image.load('../_images/star_red.bmp'),
                       pygame.image.load('../_images/star_blue.bmp'),
                       pygame.image.load('../_images/star_green.bmp'),
                       pygame.image.load('../_images/star_olive.bmp'),
                       pygame.image.load('../_images/star_purple.bmp'),
                       pygame.image.load('../_images/star_sky.bmp'))

        self.image = self.images[randint(0, len(self.images) - 1)]
        self.rect = self.image.get_rect()

        # 为每颗星星最初都设置在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = int(self.rect.height / 2)

        # 存储星星的准确位置
        self.local_x = float(self.rect.x)

    def blitme(self):
        """在指定位置绘制星星"""
        self.screen.blit(self.image, self.rect)
