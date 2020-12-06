def slope(input_array):
    slope_width = len(input_array[0])
    index = 0
    trees = 0
    for level in input_array[1:]:
        index += 3
        try:
            if level[index] == "#":
                trees += 1
        except IndexError:
            index = index - slope_width
            if level[index] == "#":
                trees += 1
    return trees


def from_txt(filepath='input.txt'):
    try:
        array = open(filepath, 'r').read().splitlines()
    except FileNotFoundError:
        filepath = input("Enter full path to input file.\n")
        array = open(filepath, 'r').read().splitlines()
    return array


if __name__ == "__main__":
    input_array = from_txt()
    print(slope(input_array))
