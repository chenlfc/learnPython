# -*- coding: utf-8 -*-
# create by o.c. 2018/8/6
# file name : game_stats.py


class GameStats():
    def __init__(self, settings):
        self.settings = settings

        self.rest_stats()
        self.game_active = True

    def rest_stats(self):
        self.people_left = self.settings.people_limit
