# -*- coding: utf-8 -*-
# create by o.c. 2018/8/6
# file name : ball.py

from random import randint
import pygame
from pygame.sprite import Sprite


class Ball(Sprite):
    """定一个颜色随机的小圆球"""

    def __init__(self, settings, screen):
        super().__init__()

        self.settings = settings
        self.screen = screen

        r_c = randint(0, self.settings.ball_mix_color)
        g_c = randint(0, self.settings.ball_mix_color)
        b_c = randint(0, self.settings.ball_mix_color)
        self.ball_color = (r_c, g_c, b_c)
        ball_x = randint(
            self.settings.ball_radius,
            self.settings.screen_width - self.settings.ball_radius)

        self.ball_centerx = ball_x
        self.ball_centery = self.settings.ball_radius

        self.rect_left = self.ball_centerx - self.settings.ball_radius
        self.rect_top = self.ball_centery - self.settings.ball_radius
        self.rect_width = self.settings.ball_radius * 2
        self.rect_height = self.rect_width
        self.rect = (self.rect_left, self.rect_top, self.rect_width,
                     self.rect_height)

    def draw_ball(self):

        pygame.draw.circle(self.screen, self.ball_color,
                           (self.ball_centerx, self.ball_centery),
                           self.settings.ball_radius)
        # self.ball_rect = ball.get_rect()
        # print(ball.center)

    def update_ball(self):
        self.ball_centery += self.settings.ball_speed_factor
        self.rect_left = self.ball_centerx - self.settings.ball_radius
        self.rect_top = self.ball_centery - self.settings.ball_radius
        self.rect_width = self.settings.ball_radius * 2
        self.rect_height = self.rect_width
        self.rect = (self.rect_left, self.rect_top, self.rect_width,
                     self.rect_height)
