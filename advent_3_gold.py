# advent of code
# anonymous user #1879507

from copy import deepcopy

with open('input_day_3.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


def get_most_common(input_list, x, rating_type):
    one_counter = 0
    zero_counter = 0
    for iterator in input_list:
        if iterator[x] == '1':
            one_counter += 1
        else:
            zero_counter += 1
    if one_counter > zero_counter and rating_type == 'oxygen':
        return '1'
    elif zero_counter > one_counter and rating_type == 'oxygen':
        return '0'
    elif one_counter > zero_counter and rating_type != 'oxygen':
        return '0'
    elif zero_counter > one_counter and rating_type != 'oxygen':
        return '1'
    elif rating_type == 'oxygen':
        return '1'
    else:
        return '0'

# a = ["1010", "1010", "0101"]
# print(get_most_common(a, 0, 'oxyagen'))


gen_rat = deepcopy(lines)
scrub_rat = deepcopy(lines)

for i in range(len(lines[0])):
    remove_gen = []
    remove_scrub = []
    most_common_o = get_most_common(gen_rat, i, 'oxygen')
    for x in range(len(gen_rat)):
        if len(gen_rat) == 1:
            break
        if gen_rat[x][i] != most_common_o:
            remove_gen.append(x)
    for x in sorted(remove_gen, reverse=True):
        gen_rat.pop(x)

    most_common_s = get_most_common(scrub_rat, i, 'scrub')
    for lx in range(len(scrub_rat)):
        if len(scrub_rat) == 1:
            break
        if scrub_rat[lx][i] != most_common_s:
            remove_scrub.append(lx)
    for lx in sorted(remove_scrub, reverse=True):
        scrub_rat.pop(lx)

print('Generator rating: %s => %s' % (gen_rat, int(gen_rat[0], 2)))
print('CO2 Scrubber rating: %s => %s' % (scrub_rat, int(scrub_rat[0], 2)))
print('Multiplied, life support rating: %s' % (int(gen_rat[0], 2) * int(scrub_rat[0], 2)))
