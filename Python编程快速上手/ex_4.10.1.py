def listToStr(ls):
    words = ''
    for s in ls:
        words += s
        if s == ls[-2]:
            words += ' and '
        elif s != ls[-1]:
            words += ', '
    return words


spam = ['apples', 'bananas', 'tofu', 'cats', 'dogs']
print(listToStr(spam))
