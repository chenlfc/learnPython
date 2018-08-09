# -*- coding: utf-8 -*-
# create by o.c. 2018/8/9
# file name : conversion_f_c.py
# description : 定义一个转换温度的类


class ConversionForC():
    """将℉与℃互相转换"""

    def __init__(self, temperature=0):
        self.temperature = temperature

    def f_to_c(self):
        """将华氏温度转换为摄氏温度并返回"""
        c_num = (self.temperature - 32) * (5 / 9)
        return c_num

    def c_to_f(self):
        """将摄氏度转换为华氏温度并返回"""
        f_num = (self.temperature * 9 / 5) + 32
        return f_num
