# advent of code
# anonymous user #1879507
from copy import deepcopy


class Path:

    def __init__(self, open_list=[], closed_list=[]):
        self.open_list = open_list
        self.closed_list = closed_list

    def get_open(self):
        return self.open_list

    def get_closed(self):
        return self.closed_list

    def set_open(self, x):
        self.open_list = x

    def set_closed(self, y):
        self.closed_list = y


class Node:

    def __init__(self, parent=None, position=None, s=0):
        self.parent = parent
        self.position = position
        self.s = s

        self.g = 0  # distance from starting node * node sums
        self.h = 0  # heuristic, estimated distance from end
        self.f = 0  # total cost => g + h

    def __eq__(self, other):  # defines comparison between nodes. equal if same position. smart.
        return self.position == other.position


def search_path(matrix, start, end):
    start_node = Node(None, start)
    end_node = Node(None, end, matrix[end[0]][end[1]])
    new_position = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # no diagonal moves
    s_multiplier = 5  # what we count as expected score per node
    results = []
    paths = [Path(open_list=[start_node], closed_list=[])]

    while len(paths) > 0:  # while we have paths keep running!! in the beginning only one
        to_be_removed = []  # which paths to delete after each loop
        to_be_added = []  # which paths to add
        for path_index, path in enumerate(paths):
            print('results: %s' % results)
            print('n_paths: %s' % len(paths))
            print('path_index: %s' % path_index)
            # loop till we find score
            if len(path.open_list) == 0:
                if path_index not in to_be_removed:
                    to_be_removed.append(path_index)
            while len(path.open_list) > 0:
                current_node = path.open_list[0]
                current_index = 0
                for i, item in enumerate(path.open_list):  # choose lowest f to iterate first
                    if item.g < current_node.g:
                        current_node = item
                        current_index = i

                # remove current item and add to closed list
                path.open_list.pop(current_index)
                path.closed_list.append(current_node)

                # if current score of path higher than the lowest result =>  delete path from path list
                if results:
                    if current_node.g >= (min(results) + 5):
                        continue
                    # if current estimation significantly larger than min result pop and break
                    if (current_node.f - len(matrix)) >= min(results):
                        continue
                # if we found goal add score and remove path
                if current_node == end_node:
                    results.append(current_node.g)
                    if path_index not in to_be_removed:
                        to_be_removed.append(path_index)
                    break

                # generate children
                children = []
                for new_pos in new_position:
                    pos = (current_node.position[0] + new_pos[0], current_node.position[1] + new_pos[1])

                    # validate borders
                    if pos[0] > (len(matrix)-1) or pos[0] < 0 or pos[1] > (len(matrix[0])-1) or pos[1] < 0:
                        continue

                    # create new node with score and add to children list
                    new_node = Node(parent=current_node, position=pos, s=matrix[pos[0]][pos[1]])
                    children.append(new_node)

                # loop children
                closed_child_count = 0
                for child in children:
                    add_to_open = True
                    # validate
                    if child in path.closed_list:
                        closed_child_count += 1
                        continue

                    child.g = child.parent.g + child.s  # have to find parents g value and add current node score
                    # heuristic => distance from end * multiplier
                    # child.h = s_multiplier * (end_node.position[0]-child.position[0]+end_node.position[1]-child.position[1])
                    # child.f = child.g + child.h  # total estimated score

                    # if child already on list
                    for open_node in path.open_list:
                        if child == open_node and child.g > open_node.g:
                            add_to_open = False
                            closed_child_count += 1
                    # add child to open list
                    if add_to_open:
                        # add new path to paths list and remove current path
                        new_path = Path()
                        for node_x in path.open_list:
                            new_path.open_list.append(node_x)
                        for node_y in path.closed_list:
                            new_path.closed_list.append(node_y)
                        new_path.open_list.append(child)
                        if new_path not in to_be_added:
                            to_be_added.append(new_path)
                        if path_index not in to_be_removed:
                            to_be_removed.append(path_index)

                if closed_child_count == len(children) and path_index not in to_be_removed:  # if no possible paths
                    to_be_removed.append(path_index)

        for item in sorted(to_be_removed, reverse=True):  # remove paths which score too high before next loop
            paths.pop(item)
        if to_be_added:
            for to_add in to_be_added:
                paths.append(to_add)

    return results


def main():
    with open('input_day_15.txt') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    matrix = []
    for line in lines:
        line_int = []
        for char in line:
            line_int.append(int(char))
        matrix.append(line_int)

    print(matrix)

    starting_square = (0, 0)
    ending_square = (len(matrix)-1, len(matrix[0])-1)
    result = search_path(matrix, starting_square, ending_square)
    print(result)


if __name__ == '__main__':
    main()
