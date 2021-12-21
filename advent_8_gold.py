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
# acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab
# => dab = 7, ab = 1, eafb = 4, acedgfb = 8
# => d = top line
# => six digits

special_outputs_sum = 0
special_digits = [2, 4, 3, 7]

for line in lines:
    input_values, output_values = line.split('|')
    input_values = input_values.rstrip().split()
    output_values = output_values.rstrip().split()

    input_values = sorted(input_values, key=len)

    for input_value in input_values:
        if len(input_value) == 2:
            right_values = input_value
        if len(input_value) == 3:
            top_value = str(input_value)
            top_value = top_value.replace(right_values[0], '')
            top_value = top_value.replace(right_values[1], '')
        if len(input_value) == 4:
            top_left_mid = str(input_value)
            top_left_mid = top_left_mid.replace(right_values[0], '')
            top_left_mid = top_left_mid.replace(right_values[1], '')

    output_value = ''

    for value in output_values:
        if len(value) == 2:
            output_value += '1'
        elif len(value) == 4:
            output_value += '4'
        elif len(value) == 3:
            output_value += '7'
        elif len(value) == 7:
            output_value += '8'
        elif len(value) == 6 and (right_values[0] not in value or right_values[1] not in value):
            output_value += '6'
        elif len(value) == 6 and (top_left_mid[0] not in value or top_left_mid[1] not in value):
            output_value += '0'
        elif len(value) == 6:
            output_value += '9'
        elif right_values[0] in value and right_values[1] in value:
            output_value += '3'
        elif top_left_mid[0] not in value or top_left_mid[1] not in value:
            output_value += '2'
        else:
            output_value += '5'

    print(output_value)

    special_outputs_sum += int(output_value)


print('-------\n' + str(special_outputs_sum))
