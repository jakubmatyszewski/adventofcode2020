import re


def passport_validator(input_array):
    valid = 0
    for entry in input_array:
        passport = entry.split()
        tmp = ':'.join(passport).split(':')
        passport_d = {tmp[i]: tmp[i + 1] for i in range(0, len(tmp), 2)}
        if len(passport_d.keys()) == 7:
            if 'cid' not in passport_d.keys():
                if check_rules(passport_d) is True:
                    valid += 1
        elif len(passport_d.keys()) == 8:
            if check_rules(passport_d) is True:
                valid += 1
    return valid


def check_rules(p):
    if all([
        1920 <= int(p['byr']) <= 2002,
        2010 <= int(p['iyr']) <= 2020,
        2020 <= int(p['eyr']) <= 2030,
        p['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
        len(p['pid']) == 9,
        re.search('#[a-f0-9]{6}', p['hcl']) is not None,
        (p['hgt'][-2:] == 'in' and 59 <= int(p['hgt'][:-2]) <= 76)
        or (p['hgt'][-2:] == 'cm' and 150 <= int(p['hgt'][:-2]) <= 193)]):
        return True


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
