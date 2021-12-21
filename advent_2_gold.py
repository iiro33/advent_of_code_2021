# advent of code
# anonymous user #1879507

with open('input_day_2.txt') as file:
    lines = file.readlines()
    lines = [line for line in lines]


horizontal_pos = 0
depth = 0
aim = 0

for line in lines:
    command, x = line.split()
    x = int(x)
    if command == 'forward':
        horizontal_pos += x
        depth += aim * x
    elif command == 'down':
        aim += x
    else:
        aim -= x
    if depth < 0:
        depth = 0


print("Horizontal position: %s,\n Depth: %s,\n Multiplied: %s" % (horizontal_pos, depth, horizontal_pos * depth))