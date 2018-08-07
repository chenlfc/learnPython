# -*- coding: utf-8 -*-
# create by o.c. 2018/7/27
# file name : alien_invasion.py

# import sys
import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

# from alien import Alien


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建一个用于存储游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    score_board = Scoreboard(ai_settings, screen, stats)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 创建一群外星人
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:

        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, score_board, ship, aliens,
                        bullets, play_button)

        if stats.game_active:
            ship.update()

            gf.update_bullets(ai_settings, screen, stats, score_board, ship,
                              aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, score_board, ship,
                             aliens, bullets)
        else:
            if stats.ships_left == 0:
                bullets.empty()
                aliens.empty()
        #     # ship = Ship(ai_settings, screen)
        #     # ai_settings.ship_image = './images/game_over.bmp'
        #     # ship.rect.centery = screen.get_rect().centery
        #     # ship.blitme()

        # 重绘屏幕
        gf.update_screen(ai_settings, screen, stats, score_board, ship, aliens,
                         bullets, play_button)


run_game()
