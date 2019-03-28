def sanitize(time_string):
    """
    获取正确地时间格式。
    参数"time_string"，表示混乱的时间格式。
    """
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string

    (mins, secs) = time_string.split(splitter)
    return mins + '.' + secs


def get_coach_data(filename):
    """
    将指定文件去除不需要的空白符并返回列表。
    参数"filename“，将要转换为列表的文件路径。
    """
    try:
        with open(filename) as fl:
            data = fl.readline().strip().split(',')
        # dt = {}
        # dt['Name'] = data.pop(0)
        # dt['Dob'] = data.pop(0)
        # dt['Times'] = sorted(set([sanitize(t) for t in data]))
        # return dt
        return {'Name': data.pop(0),
                'Dob': data.pop(0),
                'Times': (sorted(set([sanitize(t) for t in data])))}
    except IOError as err:
        print('File Error\n\t' + str(err))
        return None


def ptdit(mydit):
    """按格式输出字典参数"mydit"中的内容"""
    print(mydit['Name'] + "'s fastest times are: " +
          str(mydit['Times'][0:3]))
    print(' - Name\t\t' + mydit['Name'])
    print(' - Dob\t\t' + mydit['Dob'])
    print(' - All Times\t' + str(mydit['Times']))


sarah = get_coach_data(".//chapter6//sarah2.txt")
ptdit(sarah)
james = get_coach_data(".//chapter6//james2.txt")
ptdit(james)
julie = get_coach_data(".//chapter6//julie2.txt")
ptdit(julie)
sarah = get_coach_data(".//chapter6//sarah2.txt")
ptdit(sarah)
# dict_sarah = {}
# dict_sarah['Name'] = sarah.pop(0)
# dict_sarah['Dob'] = sarah.pop(0)
# dict_sarah['Times'] = sarah


# (sarah_name, sarah_dob) = sarah.pop(0), sarah.pop(0)
# print(sarah_name + "'s fastest times are: " +
#       str(sorted(set([sanitize(t) for t in sarah]))[0:3]))
