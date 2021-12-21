# advent of code
# anonymous user #1879507
import pandas as pd
import numpy as np

with open('input_day_13.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

folds = []
coordinates = []
max_x = 0  # to track how big zero-dataframe to create
max_y = 0
min_x = 100000
min_y = 100000

for line in lines:
    if ',' in line:
        xy = list(map(int, line.split(',')))
        coordinates.append(xy)
        if xy[0] > max_x:
            max_x = xy[0]
        if xy[1] > max_y:
            max_y = xy[1]
        if xy[0] < min_x:
            min_x = xy[0]
        if xy[1] < min_y:
            min_y = xy[1]
    elif 'fold' in line:
        cmd, n = line.split('=')
        folds.append([cmd[-1], int(n)])

# create empty data frame
df = pd.DataFrame(np.zeros((max_y + 1, max_x + 2)))

print(folds)
print(coordinates)
print('Max x: %s, Max y: %s, Min x: %s, Min y: %s' % (max_x, max_y, min_x, min_y))

# populate data frame
for pair in coordinates:
    df.loc[pair[1], pair[0]] += 1

i = 0
print('After %s folds:' % i)
print(df.where(df > 0).count().sum())

for cmd in folds:
    if cmd[0] == 'y':
        df2 = df.loc[0:cmd[1]-1, :]
        df3 = df.loc[cmd[1]+1:max(df.index), :]
        df = df2 + df3.loc[::-1].set_index(df2.index)
    else:
        df2 = df.loc[:, 0:cmd[1]-1]
        df3 = df.loc[:, cmd[1]+1:max(df.columns)]
        df3 = df3.loc[:, ::-1]
        df3.columns = range(0, cmd[1])
        df = df2 + df3
    i += 1
    print('After %s folds:' % i)
    print(df.where(df > 0).count().sum())
    if i == 12:
        print(df)

df.to_csv('asd.csv')
# CEJKLUGJ
