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


def unique_data(data):
    temp = []
    for ud in data:
        if ud not in temp:
            temp.append(ud)

    return temp


def getlist(file):
    """
    将指定文件去除不需要的空白符并返回列表。
    参数"file“，将要转换为列表的文件路径。
    """
    try:
        with open(file) as fl:
            return fl.readline().strip().split(',')
    except IOError as err:
        print('File Error\n\t' + str(err))
        return None


def ptlist(ls):
    """
    按需求输出参数”ls“列表的前3项。
    """
    print(sorted(set(ls))[0:3])


james = getlist(".//chapter5//james.txt")
julie = getlist(".//chapter5//julie.txt")
mikey = getlist(".//chapter5//mikey.txt")
sarah = getlist(".//chapter5//sarah.txt")

njames = [sanitize(t) for t in james]
njulie = [sanitize(t) for t in julie]
nmikey = [sanitize(t) for t in mikey]
nsarah = [sanitize(t) for t in sarah]

ptlist(njames)
ptlist(njulie)
ptlist(nmikey)
ptlist(nsarah)

"""
try:
    with open('.//chapter5//james.txt') as f_james, \
            open('.//chapter5//julie.txt') as f_julie,\
            open('.//chapter5//mikey.txt') as f_mikey,\
            open('.//chapter5//sarah.txt') as f_sarah:
        data = f_james.readline()
        james = data.strip().split(',')
        data = f_julie.readline()
        julie = data.strip().split(',')
        data = f_mikey.readline()
        mikey = data.strip().split(',')
        data = f_sarah.readline()
        sarah = data.strip().split(',')

        njames = [sanitize(each_t) for each_t in james]
        njulie = [sanitize(each_t) for each_t in julie]
        nmikey = [sanitize(each_t) for each_t in mikey]
        nsarah = [sanitize(each_t) for each_t in sarah]

        # unique_james = []
        # for u_t in njames:
        #     if u_t not in unique_james:
        #         unique_james.append(u_t)
        # print(unique_james)
        print(sorted(set(njames))[0:3])
        print(sorted(set(njulie))[0:3])
        print(sorted(set(nmikey))[0:3])
        print(sorted(set(nsarah))[0:3])
        # for jd in james:
        #     njames.append(sanitize(jd))
        # for jd in julie:
        #     njulie.append(sanitize(jd))
        # for md in mikey:
        #     nmikey.append(sanitize(md))
        # for sd in sarah:
        #     nsarah.append(sanitize(sd))

        # james.sort()
        # julie.sort()
        # mikey.sort()
        # sarah.sort()
        # print(sorted(njames, reverse=True))
        # print(sorted(njulie))
        # print(sorted(nmikey, reverse=True))
        # print(sorted(nsarah))
except IOError as err:
    print('File Error\n\t'+str(err))
"""
