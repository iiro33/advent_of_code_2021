# advent of code
# anonymous user #1879507

with open('input_day_1.txt') as file:
    lines = file.readlines()
    lines = [int(line) for line in lines]

counter = 0
temp_sum = 0

for i in range(len(lines) - 2):
    if temp_sum == 0:
        temp_sum = lines[0] + lines[1] + lines[2]
        continue
    if (lines[i] + lines[i+1] + lines[i+2]) > temp_sum:
        counter += 1
    temp_sum = lines[i] + lines[i+1] + lines[i+2]

print(str(counter))