from athlete import Athlete


def get_coach_data(filename):
    """
    将指定文件去除不需要的空白符并返回列表。
    参数"filename“，将要转换为列表的文件路径。
    """
    try:
        with open(filename) as fl:
            data = fl.readline().strip().split(',')

        return Athlete(data.pop(0),
                       data.pop(0),
                       data)
    except IOError as err:
        print('File Error\n\t' + str(err))
        return None


james = get_coach_data('.//chapter6//james2.txt')
julie = get_coach_data('.//chapter6//julie2.txt')
mikey = get_coach_data('.//chapter6//mikey2.txt')
sarah = get_coach_data('.//chapter6//sarah2.txt')
print(james.name + "'s fastest times are: " + str(james.top3()))
print(julie.name + "'s fastest times are: " + str(julie.top3()))
print(mikey.name + "'s fastest times are: " + str(mikey.top3()))
print(sarah.name + "'s fastest times are: " + str(sarah.top3()))
# print(james.times)
# james.add_time('0:3')
# print(james.name + "'s fastest times are: " + str(james.top3()))
# print(james.times)
# james.add_times(['3.2', '1:2', '0-1'])
# print(james.name + "'s fastest times are: " + str(james.top3()))
# print(james.times)
vera = Athlete('Vera Vi')
vera.append('1.31')
print(vera.top3())
vera.extend(['2.22', '1-21', '2:22'])
print(vera.top3())
