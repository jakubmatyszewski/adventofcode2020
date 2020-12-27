import re


def challenge(arr):
    output = {}
    mask = 36 * 'X'
    for line in arr:
        key, value = line.split(' = ')
        if line.startswith('mask'):
            mask = value
            continue
        mem = re.findall(r'\d+', key)[0]
        value = list(f'{int(value):0>36b}')
        for i, bit in enumerate(mask):
            if bit != 'X':
                value[i] = bit
        output[mem] = int(''.join(value), 2)
    return sum(output.values())


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
