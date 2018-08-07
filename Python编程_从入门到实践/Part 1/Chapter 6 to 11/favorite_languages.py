# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/22
from _for_ex import pt_title

pt_title('favorite_languages.py'.upper())

    # def get_languages(name):
    #     print(name.title() + "'s favorite language is " +
    #           favorite_languages[name].title() + ".")

    # favorite_languages = {
    #     'jen': 'python',
    #     'sarah': 'c',
    #     'edward': 'ruby',
    #     'phil': 'python',
    # }

    # for n in favorite_languages:
    #     get_languages(n)

    # pt_title("new favorite languages".title())
    # friends = ['phil', 'sarah']
    # for name in favorite_languages.keys():
    #     print(name.title())
    #     if name in friends:
    #         print(" Hi " + name.title() + ", I see your favorite language is " +
    #               favorite_languages[name] + "!")

    # if 'erin' not in favorite_languages.keys():
    #     print("Erin, please take our poll!\n")

    # for name in sorted(favorite_languages.keys()):
    #     print(name.title() + ", thank you for taking the poll.")

    # print("\nThe following languages have been mentioned:")
    # for language in set(favorite_languages.values()):
    #     print(language.title())

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())
    else:
        print("\n" + name.title() + "'s favorite languages is:" + 
            languages[0])
