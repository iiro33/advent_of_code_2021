# advent of code
# anonymous user #1879507

import pandas as pd
import numpy as np

with open('input_day_5.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

df = pd.DataFrame(np.zeros((1000, 1000)))


for line in lines:
    x, y = line.split(' -> ')
    x1, y1 = list(map(int, x.split(',')))
    x2, y2 = list(map(int, y.split(',')))
    if x1 == x2 or y1 == y2:
        df.loc[min(y1, y2):max(y1, y2), min(x1, x2):max(x1, x2)] += 1
    elif abs(x1 - x2) == abs(y1 - y2):
        for z in range(abs(x1 - x2) + 1):
            if (x1 - x2) * (y1 - y2) >= 0:
                df.loc[min(y1, y2) + z, min(x1, x2) + z] += 1
            else:
                df.loc[max(y1, y2) - z, min(x1, x2) + z] += 1

print(df.where(df > 1).count().sum())
