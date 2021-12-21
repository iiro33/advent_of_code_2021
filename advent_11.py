# advent of code
# anonymous user #1879507
import pandas as pd

with open('input_day_11.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

df = pd.DataFrame([[int(character) for character in line] for line in lines])
rows = len(df.index)
cols = len(df.columns)
iterations = 500
adjacents = [-1, 0, 1]

flashes = 0
synchronized_flashes = []

for iteration in range(iterations):
    df += 1  # increase energies
    flashed_this_round = []  # empty list to store coordinates
    while True:
        temp_flashes = flashes  # we continue looping until there are no more flashes on that round
        for i in range(rows):
            for z in range(cols):
                if df.loc[i, z] > 9 and (str(i) + ',' + str(z)) not in flashed_this_round:  # only allow flash once
                    flashes += 1
                    flashed_this_round.append(str(i) + ',' + str(z))
                    df.loc[max(0, i + min(adjacents)):min(rows - 1, i + max(adjacents)), \
                        max(0, z + min(adjacents)):min(cols - 1, z + max(adjacents))] += 1
        if temp_flashes == flashes:  # check if no flashes happened... we can move to next round
            break
    df[df > 9] = 0  # reset counter to zero for everything that flashed
    if len(flashed_this_round) == rows * cols:  # check if dumbos are flashing in sync
        synchronized_flashes.append(iteration + 1)

print('Total flashes after %s steps: %s' % (iterations, flashes))
print('Synchronized flashes: %s' % synchronized_flashes)
