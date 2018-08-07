# -*- coding: utf-8 -*-
# create by o.c. 2018/8/3
# file name : the_rain.py

# from datetime import datetime

import pygame
from pygame.sprite import Group

import rain_functions as rf
from settings import Settings


def run_game():
    pygame.init()

    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width,
                                      settings.screen_height))

    rains = Group()
    rf.create_rains(settings, screen, rains)

    stars = Group()
    rf.create_stars(settings, screen, stars)

    # start_time = datetime.now()
    # is_update_star = True

    while True:

        rf.check_event(settings, screen, stars)

        # now_time = datetime.now()
        # if (now_time - start_time).seconds % 2 == 1 and is_update_star:
        #     rf.update_stars(settings, screen, stars)
        #     is_update_star = False
        # elif (now_time - start_time).seconds % 2 != 1:
        #     is_update_star = True

        rf.update_rains(settings, screen, rains)

        pygame.display.set_caption(settings.screen_caption)

        rf.update_screen(settings, screen, rains, stars)


run_game()
