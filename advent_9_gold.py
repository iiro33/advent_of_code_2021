# advent of code
# anonymous user #1879507
import pandas as pd
# import numpy as np

with open('input_day_9.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

low_points = []
low_point_coordinates = []

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


df_max_row = len(df.index) - 1
df_max_col = len(df.columns) - 1

for i in range(len(lines)):
    for z in range(len(lines[0])):
        if check_low_point(df, i, z, df_max_row, df_max_col):
            low_points.append(df.loc[i, z])
            low_point_coordinates.append([i, z])

print(low_point_coordinates)


def get_up(i_df, x, y, previous_value, max_row, max_col, iterated_coordinates):
    value = i_df.loc[x, y]
    size = 0
    if str(x) + str(y) in iterated_coordinates:
        return size
    if value == 9:
        return size
    if value >= previous_value:
        size += 1
        iterated_coordinates.append(str(x) + str(y))
    else:
        return size
    if x - 1 >= 0:
        size += get_up(i_df, x-1, y, value, max_row, max_col, iterated_coordinates)
    if y - 1 >= 0:
        size += get_left(i_df, x, y-1, value, max_row, max_col, iterated_coordinates)
    if y + 1 <= max_col:
        size += get_right(i_df, x, y+1, value, max_row, max_col, iterated_coordinates)

    return size


def get_down(i_df, x, y, previous_value, max_row, max_col, iterated_coordinates):
    value = i_df.loc[x, y]
    size = 0
    if str(x) + str(y) in iterated_coordinates:
        return size
    if value == 9:
        return size
    if value >= previous_value:
        size += 1
        iterated_coordinates.append(str(x) + str(y))
    else:
        return size
    if x + 1 <= max_row:
        size += get_down(i_df, x+1, y, value, max_row, max_col, iterated_coordinates)
    if y - 1 >= 0:
        size += get_left(i_df, x, y-1, value, max_row, max_col, iterated_coordinates)
    if y + 1 <= max_col:
        size += get_right(i_df, x, y+1, value, max_row, max_col, iterated_coordinates)

    return size


def get_left(i_df, x, y, previous_value, max_row, max_col, iterated_coordinates):
    value = i_df.loc[x, y]
    size = 0
    if str(x) + str(y) in iterated_coordinates:
        return size
    if value == 9:
        return size
    if value >= previous_value:
        size += 1
        iterated_coordinates.append(str(x) + str(y))
    else:
        return size
    if x - 1 >= 0:
        size += get_up(i_df, x-1, y, value, max_row, max_col, iterated_coordinates)
    if x + 1 <= max_row:
        size += get_down(i_df, x+1, y, value, max_row, max_col, iterated_coordinates)
    if y - 1 >= 0:
        size += get_left(i_df, x, y-1, value, max_row, max_col, iterated_coordinates)

    return size


def get_right(i_df, x, y, previous_value, max_row, max_col, iterated_coordinates):
    value = i_df.loc[x, y]
    size = 0
    if str(x) + str(y) in iterated_coordinates:
        return size
    if value == 9:
        return size
    if value >= previous_value:
        size += 1
        iterated_coordinates.append(str(x) + str(y))
    else:
        return size
    if x - 1 >= 0:
        size += get_up(i_df, x-1, y, value, max_row, max_col, iterated_coordinates)
    if x + 1 <= max_row:
        size += get_down(i_df, x+1, y, value, max_row, max_col, iterated_coordinates)
    if y + 1 <= max_col:
        size += get_right(i_df, x, y+1, value, max_row, max_col, iterated_coordinates)

    return size


def get_basin_size(i_df, x, y, max_row, max_col):
    size = 1
    iterated_coordinates = [str(x) + str(y)]
    value = i_df.loc[x, y]
    if x > 0:
        size += get_up(i_df, x-1, y, value, max_row, max_col, iterated_coordinates)
    if x < max_row:
        size += get_down(i_df, x+1, y, value, max_row, max_col, iterated_coordinates)
    if y > 0:
        size += get_left(i_df, x, y-1, value, max_row, max_col, iterated_coordinates)
    if y < max_col:
        size += get_right(i_df, x, y+1, value, max_row, max_col, iterated_coordinates)
    return size


results = []
for pair in low_point_coordinates:
    temp_result = get_basin_size(df, pair[0], pair[1], df_max_row, df_max_col)
    print("Basin size for coordinates [x: %s, y: %s]: %s" % (pair[0], pair[1], temp_result))
    results.append(temp_result)

results = sorted(results, reverse=True)
result = results[0] * results[1] * results[2]

# 3
# 9
# 14
# 9

print('Basins multiplied: %s' % result)  # 1134 with test data
