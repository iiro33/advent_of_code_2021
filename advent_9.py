# advent of code
# anonymous user #1879507
import pandas as pd
# import numpy as np

with open('input_day_9.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

low_points = []

# creating a pandas data frame from lines in same structure as input data
df = pd.DataFrame([[int(character) for character in line] for line in lines])
# print(df)


def check_low_point(i_df, row, column, max_row, max_col): # input df and coordinates to loop if it's a lowest point
    up, down, right, left = False, False, False, False
    value = i_df.loc[row, column]
    if row == 0:
        up = True
    else:
        up = value < i_df.loc[row-1, column]
    if row == max_row:
        down = True
    else:
        down = value < i_df.loc[row+1, column]
    if column == 0:
        left = True
    else:
        left = value < i_df.loc[row, column-1]
    if column == max_col:
        right = True
    else:
        right = value < i_df.loc[row, column+1]

    return up and down and right and left


for i in range(len(lines)):
    for z in range(len(lines[0])):
        if check_low_point(df, i, z, len(df.index)-1, len(df.columns)-1):
            low_points.append(df.loc[i, z])

print('Sum of low-point risk levels: %s' % (sum(low_points) + len(low_points)))
