# advent of code
# anonymous user #1879507
import pandas as pd
import numpy as np
from copy import deepcopy


def populate_image(matrix):
    df = pd.DataFrame(np.zeros((len(matrix) * 3, len(matrix[0]) * 3)))
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == '#':
                df.loc[len(matrix) + y, len(matrix[0]) + x] += 1
    return df


def enhance_image(image, algo):
    enhanced_image = pd.DataFrame(np.zeros((len(image.index)+2, len(image.columns)+2)))
    for y in range(1, len(image.index) - 1):
        for x in range(1, len(image.columns) - 1):
            value = str(int(image.loc[y-1, x-1])) + \
                str(int(image.loc[y-1, x])) + \
                str(int(image.loc[y-1, x+1])) + \
                str(int(image.loc[y, x-1])) + \
                str(int(image.loc[y, x])) + \
                str(int(image.loc[y, x+1])) + \
                str(int(image.loc[y+1, x-1])) + \
                str(int(image.loc[y+1, x])) + \
                str(int(image.loc[y+1, x+1]))
            to_map = algo[int(value, 2)]
            if to_map == '#':
                to_map = 1
            else:
                to_map = 0
            enhanced_image.loc[y+1, x+1] = to_map
    if image.loc[1, 1] == 0:
        enhanced_image.loc[0:len(enhanced_image.index)-1, 0:1] = 1
        enhanced_image.loc[0:len(enhanced_image.index)-1, len(enhanced_image.columns)-2:len(enhanced_image.columns)-1] = 1
        enhanced_image.loc[0:1, 0:len(enhanced_image.columns)-1] = 1
        enhanced_image.loc[len(enhanced_image.index)-2:len(enhanced_image.index)-1, 0:len(enhanced_image.columns)-1] = 1
    return enhanced_image


def main():
    with open('input_day_20.txt') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    enhancing_algorithm = ''
    image = []
    test_1 = 0
    for line in lines:
        if line == '':
            test_1 = 1
            continue
        if test_1 == 1:
            image.append(line)
        else:
            enhancing_algorithm += line

    print(enhancing_algorithm)
    print(image)
    image = populate_image(image)
    for _ in range(50):
        image = enhance_image(image, enhancing_algorithm)
    print('image lit count: %s' % image.where(image > 0).count().sum())


if __name__ == '__main__':
    main()
