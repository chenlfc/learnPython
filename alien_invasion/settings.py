# -*- coding: utf-8 -*-
# create by o.c. 2018/7/27
# file name : settings.py

import json


class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        self.filenames = ['settings.json', 'high_score.json']
        for filename in self.filenames:
            with open(filename, 'r') as f_obj:
                settings = json.load(f_obj)
                self.__dict__.update(settings)

        self.initialize_dynamic_settings()
        # self.save_to_json()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction为1表示向右：为-1表示向左
        self.fleet_direction = 1

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        # print(self.alien_points)

    def save_to_json(self):
        settings = [{
            "screen_width": self.screen_width,
            "screen_height": self.screen_height,
            "bg_color": self.bg_color,
            "ship_speed_factor": 1.5,
            "ship_image": self.ship_image,
            "bullet_speed_factor": 3,
            "bullet_width": self.bullet_width,
            "bullet_max_width": self.bullet_max_width,
            "bullet_height": self.bullet_height,
            "bullet_color": self.bullet_color,
            "bullets_allower": self.bullets_allower,
            "alien_speed_factor": 1,
            "fleet_drop_speed": 10,
            "fleet_direction": self.fleet_direction,
            "ship_limit": self.ship_limit,
            "speedup_scale": self.speedup_scale,
            "alien_points": 50,
            "score_scale": self.score_scale
        }, {
            "high_score": self.high_score
        }]
        setting_index = 0
        for filename in self.filenames:
            with open(filename, 'w') as f_obj:
                json.dump(settings[setting_index], f_obj)
                setting_index += 1
