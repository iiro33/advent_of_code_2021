# advent of code
# anonymous user #1879507
from copy import deepcopy

with open('input_day_12.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

mapping = {}

# create dictionary which contains the mapping for paths both ways; dictionary of lists
for line in lines:
    source, destination = line.split('-')
    if source not in mapping:
        mapping[source] = [destination]
    else:
        mapping[source].append(destination)
    if destination not in mapping:
        mapping[destination] = [source]
    else:
        mapping[destination].append(source)


# function to get the path
def get_path(pmapping, location, current_path, visited_n, completed_paths, multi_visits=0):
    # print(current_path)  # for debugging
    for dest in pmapping[location]:
        temp_visited_n = deepcopy(visited_n)
        temp_path = deepcopy(current_path)
        temp_path.append(dest)
        if dest == 'end':
            if temp_path not in completed_paths:
                completed_paths.append(temp_path)
        elif dest.isupper():
            completed_paths = get_path(pmapping, dest, temp_path, temp_visited_n, completed_paths, multi_visits)
        elif dest.islower() and dest not in visited_n:
            temp_visited_n.append(dest)
            completed_paths = get_path(pmapping, dest, temp_path, temp_visited_n, completed_paths, multi_visits)
        elif dest.islower() and dest in visited_n and dest not in ['start', 'end'] and multi_visits < 30:
            multi_visits += 1
            completed_paths = get_path(pmapping, dest, temp_path, temp_visited_n, completed_paths, multi_visits)

    return completed_paths



# logic which populates possible paths
print('Debugging: ')
paths = get_path(mapping, 'start', ['start'], ['start'], [])
print('----------')

# print results
print('Mapping: ')
print(mapping)
print('----------')
print('Results: ')
# print('There are %s paths: ' % len(paths))
print('There are %s paths: %s' % (len(paths), paths))  # with verification of paths
results = []
start_end = ['start', 'end']
for item in paths:
    match_dict = {}
    match_dict_sum = 0
    for element in item:
        if element in match_dict:
            match_dict[element] += 1
        else:
            match_dict[element] = 0
    for k, v in match_dict.items():
        if k.islower():
            match_dict_sum += v
    if match_dict_sum <= 1:
        results.append(item)

print('-----')
print(results)
print('real results: %s' % len(results))
