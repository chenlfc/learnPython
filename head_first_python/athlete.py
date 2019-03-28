class Athlete(list):
    """
    类Athlete。
    打包与kelly教练的学院相关训练数据的类。
    a_name=学员姓名；a_dob=学员生日；a_times=学员训练成绩表。
    """

    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def showme(self):
        """格式输出实例的相关数据"""
        print('-name - ' + self.name)
        print('- dob - ' + self.dob)
        print('-times- ' + str(self.times))

    def top3(self):
        """获取前3的成绩"""
        return sorted(set([sanitize(t) for t in self]))[0:3]


class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top3(self):
        return sorted(set([sanitize(t) for t in self])[0:3])


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
