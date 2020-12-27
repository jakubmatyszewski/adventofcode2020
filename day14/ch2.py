import re


def get_addr(mask):
    if 'X' in mask:
        for b in ('0', '1'):
            yield from get_addr(mask.replace('X', b, 1))
    else:
        yield mask


def challenge(arr):
    output = {}
    mask = 36 * 'X'
    for line in arr:
        key, value = line.split(' = ')
        if line.startswith('mask'):
            mask = value
            continue
        mem = re.findall(r'\d+', key)[0]
        addr = f'{int(mem):0>36b}'
        addr_masked = ''
        for maskbit, addrbit in zip(mask, addr):
            if maskbit == '0':
                addr_masked += addrbit
            else:
                addr_masked += maskbit

        for a in get_addr(addr_masked):
            output[int(a, 2)] = int(value)

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
