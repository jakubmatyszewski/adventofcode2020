def sum_2020(input_array, target):
    sorted_ar = sorted(input_array)
    current_sum = 0
    for i, el in enumerate(sorted_ar):
        left_i = i + 1
        right_i = len(sorted_ar) - 1
        while left_i < right_i:
            current_sum = el + sorted_ar[left_i] + sorted_ar[right_i]
            if current_sum > target:
                right_i = right_i - 1
            elif current_sum < target:
                left_i += 1
            else:
                return el, sorted_ar[left_i], sorted_ar[right_i]


def from_txt(filepath='input.txt'):
    try:
        array = open(filepath, 'r').read().splitlines()
    except FileNotFoundError:
        filepath = input("Enter full path to input file.\n")
        array = open(filepath, 'r').read().splitlines()
    return list(map(int, array))  # Converting from str to int


if __name__ == "__main__":
    input_array = from_txt()
    x, y, z = sum_2020(input_array, 2020)
    print((x, y, z))
    print(f'{x} * {y} * {z} = {x*y*z}')
