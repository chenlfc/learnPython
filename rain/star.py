# -*- coding: utf-8 -*-
# create by o.c. 2018/8/3
# file name : star.py

from random import randint

import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """定义一颗星星的类"""

    def __init__(self, settings, screen):
        super().__init__()

        self.screen = screen
        self.settings = settings

        self.p_x = 1  # randint(1, settings.star_x)
        self.p_y = 1  # randint(1, settings.star_y)
        self.p_scale = randint(settings.star_min_scale,
                               settings.star_max_scale)

        self.point_lists = [[[0.5, 0.0], [1.0, 0.2887], [1.5, 0.0],
                             [1.5, 0.5774], [2, 0.8660], [1.5, 1.1547],
                             [1.5, 1.7321], [1.0, 1.4434], [0.5, 1.7421],
                             [0.5, 1.1547], [0.0, 0.8550], [0.5, 0.5774]],
                            [[0.4639, 0.6507], [0.3633, 0.0], [0.9511, 0.2968],
                             [1.5388, 0.0], [1.4382, 0.6507], [1.9021, 1.1180],
                             [1.2521, 1.2234], [0.9511, 1.8090],
                             [0.6500, 1.2234], [0.0, 1.118]]]
        self.point_list = self.point_lists[randint(0, 1)]
        self.star_point_list = []
        # print('- ', self.star_point_list)

        rgb_color = randint(settings.star_min_color, settings.star_max_color)
        if self.p_scale == settings.star_min_scale:
            rgb_color *= 2
        self.color = (rgb_color, rgb_color, rgb_color)

    def update_point_list(self):
        self.point_list = self.point_lists[randint(0, 1)]
        for x_y in self.point_list:
            temp = [(x_y[0] + self.p_x) * self.p_scale,
                    (x_y[1] + self.p_y) * self.p_scale]
            self.star_point_list.append(temp)

    def draw_star(self):
        # rgb_color = randint(self.settings.star_min_color,
        #                     self.settings.star_max_color)
        # self.color = (rgb_color, rgb_color, rgb_color)
        star_line_width = randint(0, 1)
        pygame.draw.polygon(self.screen, self.color, self.star_point_list,
                            star_line_width)
