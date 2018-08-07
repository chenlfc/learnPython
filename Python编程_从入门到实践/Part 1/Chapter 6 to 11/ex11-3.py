# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/26
import unittest
from _for_ex import pt_title
from employee import Employee

pt_title('EX 11 - 3')


# EX 11-3
class EmployeeTest(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('jack', 'lee', 30000)

    def test_give_default_raise(self):
        self.employee.give_raise()

    def test_give_custom_raise(self):
        self.employee.give_raise(4500)


unittest.main()
