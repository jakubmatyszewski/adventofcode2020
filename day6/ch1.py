def custom_customs(input_array):
    groups = [group.replace('\n', '') for group in input_array]
    return sum([len(set(group)) for group in groups])


def from_txt(filepath='input.txt'):
    try:
        array = open(filepath, 'r').read()
    except FileNotFoundError:
        filepath = input("Enter full path to input file.\n")
        array = open(filepath, 'r').read()
    groups = array.split('\n\n')
    return groups


if __name__ == "__main__":
    input_array = from_txt()
    print(custom_customs(input_array))
