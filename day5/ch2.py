def binary_boarding(input_array):
    seatIDs = []
    for entry in input_array:
        scheme = {'F': '0', 'L': '0', 'B': '1', 'R': '1'}
        for key, value in scheme.items():
            entry = entry.replace(key, value)
        row = int(entry[:7], 2)
        column = int(entry[7:], 2)
        seatIDs.append(row * 8 + column)
    myID = set(list(range(min(seatIDs), max(seatIDs) + 1))) - set(seatIDs)
    return int(myID)


def from_txt(filepath='input.txt'):
    try:
        array = open(filepath, 'r').read().splitlines()
    except FileNotFoundError:
        filepath = input("Enter full path to input file.\n")
        array = open(filepath, 'r').read().splitlines()
    return array


if __name__ == "__main__":
    input_array = from_txt()
    print(binary_boarding(input_array))
