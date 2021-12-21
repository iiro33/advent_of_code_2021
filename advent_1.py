# advent of code
# anonymous user #1879507

with open('input_day_1.txt') as file:
    lines = file.readlines()
    lines = [int(line) for line in lines]

temp = 0
counter = 0
for i in lines:
    if temp == 0:
        temp = i
        continue
    if i > temp:
        counter += 1
    temp = i

print(str(counter))