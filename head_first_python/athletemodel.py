import pickle
from athletelist import AthleteList


def get_coach_data(filename):
    """
    将指定文件去除不需要的空白符并返回列表。
    参数"filename“，将要转换为列表的文件路径。
    """
    try:
        with open(filename) as fl:
            data = fl.readline().strip().split(',')

        return AthleteList(data.pop(0),
                           data.pop(0),
                           data)
    except IOError as err:
        print('File Error\n\t' + str(err))
        return None


def put_to_store(files_list):
    try:
        all_athletes = {}
        for filename in files_list:
            with open(filename) as fldata:
                all_athletes[filename] = fldata.readline().strip()

        with open('alldata.dat', 'wb') as alldata:
            pickle.dump(all_athletes, alldata)
    except IOError as err:
        print('File Error\n\t' + str(err))
    except pickle.PickleError as err:
        print('PickleError\n\t' + str(err))

    return all_athletes


def get_from_store():
    all_athletes = {}
    with open('alldata.dat', 'rb') as alldata:
        all_athletes = pickle.load(alldata)
    return all_athletes


files_list = ['.//chapter6//james2.txt',
              './/chapter6//julie2.txt',
              './/chapter6//mikey2.txt',
              './/chapter6//sarah2.txt']

print(put_to_store(files_list))
print(get_from_store())
