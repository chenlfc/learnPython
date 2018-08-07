# 恭喜你，可以进行一次考试了
# 修正别人代码中的错误

from sys import argv
f = open(argv[1], "w", encoding="utf-8")


def print_to_file(strings):
    print(strings)
    strings += '\n'
    f.write("%s" % strings)


def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words


def sort_words(words):
    """Sorts the words."""
    return sorted(words)


def print_first_word(words):  # 这里漏了冒号:
    """Prints the first word after popping it off."""
    word = words.pop(0)  # 这里poop多了个o
    print_to_file(word)  # 这里是版本问题，print需要加上()，以下所有print都会有这个问题


def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)  # 这里漏了括号的右半边)
    print_to_file(word)


def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print_to_file("Let's practice everything.")

print_to_file(
    'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print_to_file("--------------")
print_to_file(poem)
print_to_file("--------------")

five = 10 - 2 + 3 - 6
print_to_file("This should be five: %d" % five)


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print_to_file("With a starting point of: %d" % start_point)
print_to_file("We'd have %d jeans, %d jars, and %d crates." %
              (beans, jars, crates))

start_point = start_point / 10

print_to_file("We can also do that this way:")
print_to_file("We'd have %d beans, %d jars, and %d crabapples." %
              secret_formula(start_point))


sentence = "All god\tthings come to those who weight."

words = break_words(sentence)
sorted_words = sort_words(words)

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words = sort_sentence(sentence)
print_to_file(sorted_words)

print_first_and_last(sentence)
print_first_and_last_sorted(sentence)
