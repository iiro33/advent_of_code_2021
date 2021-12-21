# advent of code
# anonymous user #1879507


def get_versions(i, string):
    version_sum = int(string[i:i+3], 2)
    type_id = int(string[i+3:i+6], 2)
    i += 6
    if type_id == 4:
        while True:
            i += 5  # loop each literal
            if string[i-5] == '0':  # last literal
                break
    else:
        if string[i] == '0':
            end_index = i + 16 + int(string[i+1:i+16], 2)
            i += 16
            while i < end_index:
                i, v = get_versions(i, string)
                version_sum += v
        else:
            n_packets = int(string[i+1:i+12], 2)
            i += 12
            for _ in range(n_packets):
                i, v = get_versions(i, string)
                version_sum += v

    return i, version_sum


def main():
    with open('input_day_16.txt') as file:
        lines = file.readlines()
        og_string = lines[0].rstrip()

    # convert to binary and store new string
    string = ''
    for char in og_string:
        string += bin(int(char, 16))[2:].zfill(4)  # add leading zeroes

    print('og: %s' % og_string)
    print('in binary: %s' % string)

    end_index, version_numbers = get_versions(0, string)

    print(end_index)
    print(version_numbers)


if __name__ == '__main__':
    main()
