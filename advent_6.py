# advent of code
# anonymous user #1879507

with open('input_day_6.txt') as file:
    lines = file.readlines()

internals = list(map(int, lines[0].split(',')))

for i in range(80):
    internals = [item - 1 for item in internals]
    z = 0
    for element in internals:
        if element < 0:
            internals[z] = 6
            internals.append(8)
        z += 1

# after 80 days
print(len(internals))

internals = list(map(int, lines[0].split(',')))
from collections import Counter
internals = dict(Counter(internals))

for i in range(256):    
    internals = {i: (0 if internals.get(i + 1) is None else internals.get(i + 1)) for i in range(-1, 8)}
    # make all 8s -1 because we create new fish with 8 after it reaches 0
    internals[8] = internals[-1]
    # add new internals to that are exhausted
    internals[6] += internals[-1]
    # reset exhausted internals
    internals[-1] = 0 

# after 256 days
print(sum(internals.values()))