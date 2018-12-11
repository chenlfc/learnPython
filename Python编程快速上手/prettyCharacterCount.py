import pprint
message = 'It was a bright cold day in Apirl, ' \
    'and the clocks were striking thirteen.'
count = {}

for charactor in message:
    count.setdefault(charactor, 0)
    count[charactor] = count[charactor] + 1

pprint.pprint(count)
print(count)