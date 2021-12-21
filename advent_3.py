# advent of code
# anonymous user #1879507

with open('input_day_3.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

gamma = ''
epsilon = ''

for i in range(len(lines[0])):
    ones = 0
    zeroes = 0
    for line in lines:
        if line[i] == '1':
            ones += 1
        else:
            zeroes += 1
    if ones > zeroes:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print('Gamma rate: %s => %s' % (gamma, int(gamma, 2)))
print('Epsilon rate: %s => %s' % (epsilon, int(epsilon, 2)))
print('Multiplied: %s' % (int(gamma, 2) * int(epsilon, 2)))
