# -*- coding: utf-8 -*-
# create by o.c. 2018/8/6
# file name : grasp_ball.py

import pygame
from pygame.sprite import Group

from settings import Settings
from people import People
from game_stats import GameStats
import grasp_ball_functions as gbf


def grasp_ball():
    pygame.init()

    settings = Settings()

    screen = pygame.display.set_mode((settings.screen_width,
                                      settings.screen_height))
    pygame.display.set_caption(settings.screen_caption)
    stats = GameStats(settings)

    people = People(settings, screen)

    balls = Group()

    gbf.create_ball(settings, screen, balls)

    while True:
        gbf.check_events(people)

        if stats.game_active:
            gbf.update_ball(settings, stats, screen, people, balls)

        else:
            balls.empty()
            settings.people_image = './images/game_over.bmp'
            people = People(settings, screen)
            people.rect.centerx = screen.get_rect().centerx
            people.rect.centery = screen.get_rect().centery
            people.draw_people()

        gbf.update_screen(settings, screen, people, balls)


grasp_ball()
