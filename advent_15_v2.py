# advent of code
# anonymous user #1879507


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

    def __lt__(self, other):
        return self.f < other.f


def search_path(matrix, start, end):
    start_node = Node(None, start)
    end_node = Node(None, end, matrix[end[0]][end[1]])
    new_position = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # no diagonal moves
    s_multiplier = 2  # what we count as expected score per node
    results = []
    open_list = []
    closed_list = []
    open_list.append(start_node)

    while len(open_list) > 0:
        open_list.sort()
        current_node = open_list.pop(0)
        closed_list.append(current_node)

        # if we found goal add score and remove path
        if current_node == end_node:
            results.append(current_node.g)
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
            if new_node in closed_list:
                continue
            else:
                children.append(new_node)

        # loop children
        for child in children:
            add_to_open = True
            # validate
            if child in closed_list:
                continue

            child.g = child.parent.g + child.s  # have to find parents g value and add current node score
            # heuristic => distance from end * multiplier
            child.h = s_multiplier * (end_node.position[0]-child.position[0]+end_node.position[1]-child.position[1])
            child.f = child.g + child.h  # total estimated score

            # if child already on list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    add_to_open = False
            # add child to open list
            if add_to_open:
                open_list.append(child)

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

    starting_square = (0, 0)
    ending_square = (len(matrix)-1, len(matrix[0])-1)
    result = search_path(matrix, starting_square, ending_square)
    print(result)


if __name__ == '__main__':
    main()
