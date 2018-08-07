# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/26
import unittest
from _for_ex import pt_title
from city_functions import get_formatted_city

pt_title('EX 11 - 1')


# EX 11-1
class CityFormattedTest(unittest.TestCase):
    """用于测试get_formatted_city模块"""

    def test_formatted_city_country(self):
        """能够正确的返回像Santiago, Chile"""
        formatted_city = get_formatted_city('santiago', 'chile')
        self.assertEqual(formatted_city, 'Santiago, Chile')

    def test_formatted_city_country_population(self):
        """能够正确地返回像Santiago, Chile - population 5000000"""
        formatted_city = get_formatted_city(
            'santiago', 'chile', population=5000000)
        self.assertEqual(formatted_city,
                         'Santiago, Chile - population 5000000')


unittest.main()
