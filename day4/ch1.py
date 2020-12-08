def passport_validator(input_array):
    valid = 0
    for entry in input_array:
        passport = entry.split()
        tmp = ':'.join(passport).split(':')
        passport_d = {tmp[i]: tmp[i + 1] for i in range(0, len(tmp), 2)}
        if len(passport_d.keys()) == 7:
            if 'cid' not in passport_d.keys():
                valid += 1
        elif len(passport_d.keys()) == 8:
            valid += 1
    return valid


def from_txt(filepath='input.txt'):
    try:
        array = open(filepath, 'r').read()
    except FileNotFoundError:
        filepath = input("Enter full path to input file.\n")
        array = open(filepath, 'r').read()
    entries = array.split('\n\n')
    return entries


if __name__ == "__main__":
    input_array = from_txt()
    print(passport_validator(input_array))
