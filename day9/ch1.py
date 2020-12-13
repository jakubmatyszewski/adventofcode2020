def encoding_error(input_array):
    for min_preamble, entry in enumerate(input_array):
        max_preamble = min_preamble + 5
        preamble = sorted(input_array[min_preamble:max_preamble])
        left_i = 0
        right_i = 4
        lookup = input_array[max_preamble]
        current_sum = 0
        while True:
            current_sum = preamble[left_i] + preamble[right_i]
            if current_sum > lookup:
                right_i = right_i - 1
            elif current_sum < lookup:
                left_i += 1
            else:
                break
            if left_i >= right_i:
                return input_array[max_preamble]


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
    print(encoding_error(input_array))
