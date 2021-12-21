# advent of code
# anonymous user #1879507

with open('input_day_2.txt') as file:
    lines = file.readlines()
    lines = [line for line in lines]


horizontal_pos = 0
depth = 0

for line in lines:
    command = line.split()
    if command[0] == 'forward':
        horizontal_pos += int(command[1])
    elif command[0] == 'down':
        depth += int(command[1])
    else:
        depth -= int(command[1])
    if depth < 0:
        depth = 0


print("Horizontal position: %s,\n Depth: %s,\n Multiplied: %s" % (horizontal_pos, depth, horizontal_pos * depth))