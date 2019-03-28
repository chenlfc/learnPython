#! Python3.7
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip

# oldText = 'Lists of animals\nLists of aquarium life\nLists of biologists' + \
#           ' by author abbreviation\nLists of cuitivars'

# pyperclip.copy(oldText)

text = pyperclip.paste()

# Separate lines and add stars.
# 分离行并添加星号
lines = text.split('\n')
for i in range(len(lines)):  # loop through all indexes in the 'lines' list
    lines[i] = '* ' + lines[i]  # add star to each string in 'lines' list

text = '\n'.join(lines)

pyperclip.copy(text)
