# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/26
class Employee():
    """雇员信息类，用于存储雇员的一些基本信息"""

    def __init__(self, first_name, last_name, annual_salary):
        """根据参数生成全名及保存属性"""
        self.fullname = (first_name + ' ' + last_name).title()
        self.annual_salary = annual_salary

    def give_raise(self, new_raise=5000):
        """增加年薪"""
        self.annual_salary += new_raise

    def show_info(self):
        """个性化输出"""
        print(self.fullname + "\n- annual salary " + str(self.annual_salary))
