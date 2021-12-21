# advent of code
# anonymous user #1879507

from math import floor

with open('input_day_7.txt') as file:
    lines = file.readlines()

coordinates = list(map(int, lines[0].split(',')))

# print('Min: %s, Max: %s, Mean: %s' % (min(coordinates), max(coordinates), sum(coordinates)/len(coordinates)))


def get_cum_sum(nr):
    if nr == 0:
        return 0
    else:
        cum_sum = 0
        for z in range(1, nr+1):
            cum_sum += z
        return cum_sum


fuels_used = []

for i in range(min(coordinates), max(coordinates)+1):
    fuel_used = [get_cum_sum(abs(crab - i)) for crab in coordinates]
    fuels_used.append(sum(fuel_used))

print(min(fuels_used))
