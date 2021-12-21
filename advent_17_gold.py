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

    n_paths = 0
    paths = []

    for x in range(20, 235):
        if x % 5 == 0:
            print('x %s' % x)
        for y in range(-100, 3500):
            position = [0, 0]  # initial position
            x_vel = x
            y_vel = y
            for _ in range(50000):
                # add position to successful launches
                # check if we are in the target square

                if position[0] > target[1] or position[1] < target[2]:  # check if any over limits
                    break
                elif position[0] >= target[0] and position[0] <= target[1] and position[1] >= target[2] and position[1] <= target[3]:
                    n_paths += 1
                    paths.append(x)
                    break
                position[0] += x_vel
                position[1] += y_vel
                if x_vel > 0:
                    x_vel -= 1
                y_vel -= 1

    print(sorted(paths))
    print('maximum available paths: %s' % n_paths)


if __name__ == '__main__':
    main()
