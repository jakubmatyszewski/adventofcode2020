def check_psswd(input_array):
    valid = 0
    for i in input_array:
        info, string = i.split(': ')
        rang, char = info.split(' ')
        min_n, max_n = map(lambda x: x - 1, map(int, rang.split('-')))
        if (string[min_n] is char and string[max_n] is not char
            or string[min_n] is not char and string[max_n] is char):
            valid += 1
    return valid


def from_txt(filepath='input.txt'):
    try:
        array = open(filepath, 'r').read().splitlines()
    except FileNotFoundError:
        filepath = input("Enter full path to input file.\n")
        array = open(filepath, 'r').read().splitlines()
    return array


if __name__ == "__main__":
    input_array = from_txt()
    print(check_psswd(input_array))
