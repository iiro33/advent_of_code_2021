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
def get_path(pmapping, location, current_path, visited_n, completed_paths):
    # print(current_path)  # for debugging
    for dest in pmapping[location]:
        temp_visited_n = deepcopy(visited_n)
        temp_path = deepcopy(current_path)
        temp_path.append(dest)
        if dest == 'end':
            if temp_path not in completed_paths:
                completed_paths.append(temp_path)
        elif dest.isupper():
            completed_paths = get_path(pmapping, dest, temp_path, temp_visited_n, completed_paths)
        elif dest.islower() and dest not in visited_n:
            temp_visited_n.append(dest)
            completed_paths = get_path(pmapping, dest, temp_path, temp_visited_n, completed_paths)

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
print('There are %s paths: ' % len(paths))
# print('There are %s paths: %s' % (len(paths), paths))  # with verification of paths
