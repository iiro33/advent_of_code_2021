# advent of code
# anonymous user #1879507
import re


def main():
    with open('input_day_17.txt') as file:
        lines = file.readlines()

    # read target square... '-' sign is optional
    target = list(map(int, re.findall("-?\\d+", lines[0])))

    print(lines)
    print(target)

    max_y = -99999  # track highest y
    paths = []  # list of successful probe launches :D

    for x in range(100):
        for y in range(3000):
            position = [0, 0]  # initial position
            path = []  # track path
            x_vel = x
            y_vel = y
            for _ in range(500):
                # add position to successful launches
                path.append(tuple(position))
                # check if we are in the target square
                if position[0] >= target[0] and position[0] <= target[1] and position[1] >= target[2] and position[1] <= target[3]:
                    paths.append(path)
                    break
                position[0] += x_vel
                position[1] += y_vel
                if x_vel > 0:
                    x_vel -= 1
                elif x_vel < 0:
                    x_vel += 1
                y_vel -= 1

    for path in paths:  # populate max_y with highest y from successful paths
        for pos in path:
            if pos[1] > max_y:
                max_y = pos[1]

    print('max y for any: %s' % max_y)


if __name__ == '__main__':
    main()
