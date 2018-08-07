# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/25
from _for_ex import pt_title

pt_title('word_count.py'.upper())


def count_words(filename):
    try:
        with open(path + filename, encoding='utf-8') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) +
              " words.")


path = './/_txts//'
filenames = [
    'alice_in_wonderland.txt', 'maupassant.txt', 
    'hints_on_child-training.txt', 'limitations.txt', 'hideline.txt'
]
for filename in filenames:
    count_words(filename)
