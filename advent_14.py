# advent of code
# anonymous user #1879507
import regex as re
from collections import Counter
from operator import itemgetter

with open('input_day_14.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

mapping = []

for line in lines:
    if '-' in line:
        mapping.append(line.split(' -> '))  # create mapping list
    elif line == '':
        continue
    else:
        og_string = line

print('Mapping: %s' % mapping)
print('Template: %s' % og_string)

rounds = 10  # how many rounds to do?
new_string = og_string

for round_nr in range(rounds):
    added = 0
    replacement_list = []  # store to be replaced as [0] char to be added and [1] index where
    for pair in mapping:
        matches = re.finditer(pair[0], new_string, overlapped=True)
        for match in matches:
            replacement_list.append([pair[1], match.start()])
    for replacement in sorted(replacement_list, key=itemgetter(1)):
        char = replacement[0]
        i = replacement[1] + 1 + added
        new_string = new_string[0:i] + char + new_string[i:]
        added += 1

    # print('After step %s: %s' % (round_nr+1, new_string))
    print('After step %s:' % (round_nr + 1))

    commons = Counter(new_string)
    print('Length of new string: %s' % len(new_string))
    most_common_c = commons.most_common()[0]
    least_common_c = commons.most_common()[-1]
    print('Most common char: %s, %s' % (most_common_c[0], most_common_c[1]))
    print('Least common char: %s, %s' % (least_common_c[0], least_common_c[1]))
    print('result: %s' % (most_common_c[1]-least_common_c[1]))
