def pass_the_jolt(input_array):
    jolts = [0] + sorted(input_array) + [max(input_array) + 3]

    combinations = [1]
    for i in range(1, len(jolts)):
        ans = 0
        for j in range(i):
            if jolts[j] + 3 >= jolts[i]:
                ans += combinations[j]
        combinations.append(ans)
    return combinations[-1]


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
