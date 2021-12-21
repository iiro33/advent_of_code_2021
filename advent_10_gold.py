# advent of code
# anonymous user #1879507
from math import floor

with open('input_day_10.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

# example of corrupted line
# example = '{([(<{}[<>[]}>{[]{[(<()>'
# stop on first character

#print(lines)
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


def complete_closers(text, legit_openers):
    result = ''
    opened = 0
    openers = []
    for char in text:
        if char in legit_openers:
            opened += 1
            openers.append(char)
        elif check_closer(openers[-1], char):
            opened -= 1
            del openers[-1]

    for i in reversed(openers):
        result += add_closer(i)

    return result


def add_closer(opener):
    if opener == '(':
        return ')'
    elif opener == '[':
        return ']'
    elif opener == '{':
        return '}'
    else:
        return '>'


score_mapping = {')': 1, ']': 2, '}': 3, '>': 4}
scores = []
completions = []

for line in lines:
    temp_result = check_corruption(line, legit_openers)
    if temp_result == 'ok':
        completions.append(complete_closers(line, legit_openers))
    else:
        continue

for text in completions:
    score = 0
    for character in text:
        score = score * 5 + score_mapping[character]
    scores.append(score)

print(completions)
print(scores)
print('Middle score: %s' % sorted(scores)[floor(len(scores) / 2)])
