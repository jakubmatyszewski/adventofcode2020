def sum_2020(input_array, target):
    sorted_array = sorted(input_array)
    left_i = 0
    right_i = len(sorted_array) - 1
    current_sum = 0
    while (left_i < right_i):
        current_sum = sorted_array[left_i] + sorted_array[right_i]
        if current_sum > target:
            right_i = right_i - 1
        elif current_sum < target:
            left_i += 1
        else:
            return sorted_array[left_i], sorted_array[right_i]


def from_txt(filepath='input.txt'):
    try:
        array = open(filepath, 'r').read().splitlines()
    except FileNotFoundError:
        filepath = input("Enter full path to input file.\n")
        array = open(filepath, 'r').read().splitlines()
    return list(map(int, array))  # Converting from str to int


if __name__ == "__main__":
    input_array = from_txt()
    x, y = sum_2020(input_array, 2020)
    print((x, y))
    print(f'{x} * {y} = {x*y}')
