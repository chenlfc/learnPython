# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/26
# from _for_ex import pt_title

# pt_title('name_function.py'.upper())


def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name.
    
    Arguments:
        first {str} -- [first name]
        middle {str} -- [middle name]
        last {str} -- [last name]
    
    Returns:
        [str] -- [full name]
    """
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()
