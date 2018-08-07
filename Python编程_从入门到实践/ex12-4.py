# -*- coding: utf-8 -*-
# create by o.c. 2018/7/30
# file name : ex12-4.py

import sys
import pygame


def run_game():
    pygame.init()
    pygame.display.set_mode((800, 450))
    pygame.display.set_caption('==> EX 12 - 4 <==')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)
        pygame.display.flip()


run_game()
