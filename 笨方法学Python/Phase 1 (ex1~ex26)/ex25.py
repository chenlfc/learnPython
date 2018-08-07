# 更多更多的练习
def break_words(stuff):
    """This function will break up words for us.
    这个函数将为我们分解单词并返回"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words.
    对单词排序"""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off.
    把第一个单词打印出来"""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off.    
    把最后一个单词打印出来"""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and return the sorted words.
    取一个完整的句子，返回对它排序后的单词"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence
    打印句子的第一个和最后一个词"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words the prints the first and last one.
    把单词进行排序，然后打印第一个和最后一个"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

