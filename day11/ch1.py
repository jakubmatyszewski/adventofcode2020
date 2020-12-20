def rotation(arr):
    new_arr = []
    xd = len(arr)  # x dimension
    yd = len(arr[0])  # y dimension
    for row in range(xd):
        tmp_row = ''
        for col in range(yd):
            adj = []
            for x in (-1, 0, 1):
                for y in (-1, 0, 1):
                    if x == y == 0:
                        continue
                    elif (0 <= row + x < xd and 0 <= col + y < yd):
                        adj.append(arr[row + x][col + y])
            if arr[row][col] == 'L' and '#' not in adj:
                tmp_row += '#'
            elif arr[row][col] == '#' and adj.count('#') >= 4:
                tmp_row += 'L'
            else:
                tmp_row += arr[row][col]
        new_arr.append(tmp_row)
    return new_arr


def challenge(arr):
    while True:
        output = rotation(arr)
        if output == arr:
            return ''.join(arr).count('#')
        arr = output


def from_txt(filepath='input.txt'):
    try:
        array = open(filepath, 'r').read().splitlines()
    except FileNotFoundError:
        filepath = input("Enter full path to input file.\n")
        array = open(filepath, 'r').read().splitlines()
    return array


if __name__ == "__main__":
    input_array = from_txt()
    print(challenge(input_array))
