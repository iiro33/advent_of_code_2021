# advent of code
# anonymous user #1879507


with open('input_day_10.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

# example of corrupted line
# example = '{([(<{}[<>[]}>{[]{[(<()>'
# stop on first character

# print(lines)
legit_openers = ['(', '[', '{', '<']


def check_closer(opener, closer):
    if opener == '(' and closer == ')':
        return True
    elif opener == '[' and closer == ']':
        return True
    elif opener == '{' and closer == '}':
        return True
    elif opener == '<' and closer == '>':
        return True
    else:
        return False


def check_corruption(text, legit_openers):
    result = 'ok'
    opened = 0
    openers = []
    for char in text:
        if char in legit_openers:
            opened += 1
            openers.append(char)
        elif not check_closer(openers[-1], char):
            return char
        else:
            opened -= 1
            del openers[-1]
    return result


scores = []
score_mapping = {')': 3, ']': 57, '}': 1197, '>': 25137}

for line in lines:
    temp_result = check_corruption(line, legit_openers)
    if temp_result == 'ok':
        continue
    else:
        scores.append(score_mapping[temp_result])

print('Score: %s' % sum(scores))

# ()[[]]
# 1 => opened = 1, openers = ['(']
# 2 => opened = 0, if '(' and ')' ok
# 3 => opened = 1, openers = ['[']
# 4 => opened = 2, openers = ['[', '[']
# 5 ...
# 6 ...
