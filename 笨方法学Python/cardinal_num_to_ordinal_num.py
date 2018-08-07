def cardinalToOrdinal(cardinal_number):
    '''自定义函数，用于将基数转换为对应的序数并返回'''
    if cardinal_number == 0:
        ordinal_number = '1st'
    elif cardinal_number == 1:
        ordinal_number = '2nd'
    elif cardinal_number == 2:
        ordinal_number = '3rd'
    elif cardinal_number == 22:
        ordinal_number = '23rd'
    else:
        ordinal_number = str(cardinal_number + 1) + 'th'
    return ordinal_number
