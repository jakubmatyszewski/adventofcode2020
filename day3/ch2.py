from functools import reduce


def slope(input_array, right, down):
    slope_width = len(input_array[0])
    index = 0
    trees = 0
    for level in input_array[::down][1:]:
        index += right
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
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    results = [slope(input_array, i[0], i[1]) for i in slopes]
    print(reduce(lambda x, y: x * y, results))
