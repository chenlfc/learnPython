# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/26
# from _for_ex import pt_title
# pt_title('city_functions.py'.upper())


def get_formatted_city(city, country, population=0):
    """格式化城市与国家信息并返回标准格式"""
    formatted_city = city + ', ' + country
    if population == 0:
        return formatted_city.title()
    else:
        formatted_population = ' - population ' + str(population)
        return formatted_city.title() + formatted_population
