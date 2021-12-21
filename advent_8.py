# advent of code
# anonymous user #1879507


with open('input_day_8.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


# special digits are
# 1 => two signals
# 4 => four signals
# 7 => three signals
# 8 => seven signals
special_outputs_count = 0
special_digits = [2, 4, 3, 7]

for line in lines:
    input_values, output_values = line.split('|')
    input_values = input_values.rstrip().split()
    output_values = output_values.rstrip().split()
    for value in output_values:
        if len(value) in special_digits:
            special_outputs_count += 1


print(special_outputs_count)
