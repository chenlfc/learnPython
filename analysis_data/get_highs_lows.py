# -*- coding: utf-8 -*-
# create by o.c. 2018/8/9
# file name : get_highs_low.py
# description : 获取指定文件中日期列表对应的最高气温列表与最低气温列表

import csv
import sys
from datetime import datetime


class GetHighsAndLows():
    """获取指定CSV文件中的日期列表与最高最低气温列表"""

    def __init__(self, filename):
        self.filename = filename

        if self.get_file():
            self.get_datas()
        else:
            sys.exit()

    def get_datas(self):
        """获取数据集"""
        self.dates = []
        self.highs = []
        self.lows = []
        for row in self.reader:
            try:
                current_date = datetime.strptime(row[0], "%Y-%m-%d")
                high = int(row[1])
                low = int(row[3])
            except ValueError:
                print(current_date, 'missing data')
            else:
                self.dates.append(current_date)
                self.highs.append(high)
                self.lows.append(low)

    def get_file(self):
        """打开文件并获取内容"""
        try:
            self.f_obj = open(self.filename)
            self.reader = csv.reader(self.f_obj)
            self.header_row = next(self.reader)
        except FileNotFoundError:
            print("ERROR: '" + self.filename + "' Not Found!")
            return False
        return True
