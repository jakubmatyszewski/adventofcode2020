def pass_the_jolt(input_array):
    jolts = [0] + sorted(input_array) + [max(input_array) + 3]
    ones = sum([1 for i, j in zip(jolts[:-1], jolts[1:]) if j - i == 1])
    threes = sum([1 for i, j in zip(jolts[:-1], jolts[1:]) if j - i == 3])
    return ones * threes


def from_txt(filepath='input.txt'):
    try:
        array = open(filepath, 'r').read().splitlines()
    except FileNotFoundError:
        filepath = input("Enter full path to input file.\n")
        array = open(filepath, 'r').read().splitlines()
    array = [int(i) for i in array]
    return array


if __name__ == "__main__":
    input_array = from_txt()
    print(pass_the_jolt(input_array))
