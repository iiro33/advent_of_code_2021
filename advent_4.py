# advent of code
# anonymous user #1879507

import re

with open('input_day_4.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


bingoes = []
temp_bingo = []

for line in lines:
    if ',' in line:
        random_numbers = line.split(',')
    if line == '' and temp_bingo:
        bingoes.append(temp_bingo)
        temp_bingo = []
        continue
    if ',' not in line and line != '':
        temp_bingo.append(line.split())


def get_winner(bingo, nr):
    nr = int(nr)
    sum_of_numbers = 0
    for row in bingo:
        for e in row:
            if e == '':
                continue
            sum_of_numbers += int(e)
    return str(nr*sum_of_numbers)


# print winning number (last) * remaining numbers
for random_number in random_numbers:
    bingoes = [[[re.sub(r"\b%s\b" % random_number, '', x) for x in l] for l in y] for y in bingoes]
    bingo_iter = 0
    winner = []
    for bingo in bingoes:
        for i in range(5):
            tester_1 = 0
            tester_2 = 0
            for y in range(5):
                if bingo[i][y] == '':
                    tester_1 += 1
                if bingo[y][i] == '':
                    tester_2 += 1
                if tester_1 >= 5 or tester_2 >= 5:
                    print(get_winner(bingo, random_number))
                    winner.append(bingo_iter)
                    break
            if tester_1 >= 5 or tester_2 >= 5:
                break

        bingo_iter += 1
    for winner_iter in sorted(winner, reverse=True):
        del bingoes[winner_iter]

# first number is gold
# last number is silver

