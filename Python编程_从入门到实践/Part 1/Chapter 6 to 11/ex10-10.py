# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/26
from _for_ex import pt_title

pt_title('EX 10 - 10')
# EX 10-10
path = './/_txts//'
# filenames = [
#     'alice_in_wonderland.txt', 'hints_on_child-training.txt',
#     'limitations.txt', 'maupassant.txt'
# ]
filenames = ['temp.txt']

for filename in filenames:
    words = []
    with open((path + filename), encoding='utf-8') as f_object:
        lines = f_object.readlines()
        # 统计在文本中出现过的所有单词
        for line in lines:
            line = line.replace('\n', '')
            words += line.split(' ')
        words = sorted(set(words))
        print(words)

        for word in words:
            count = 0
            find_txt = word
            for line in lines:
                count += line.lower().count(find_txt)
            print("The '" + find_txt + "' in " + filename + " have " + str(count) + ".")
