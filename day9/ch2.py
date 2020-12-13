def encryption_weakness(input_array, target):
    start = 0
    curr_sum = 0
    for i, val in enumerate(input_array):
        curr_sum += val
        while curr_sum > target:
            curr_sum -= input_array[start]
            start += 1
        if curr_sum == target:
            small = min(input_array[start:i + 1])
            large = max(input_array[start:i + 1])
            return small + large


def encoding_error(input_array):
    for min_preamble, entry in enumerate(input_array):
        max_preamble = min_preamble + 25
        preamble = sorted(input_array[min_preamble:max_preamble])
        left_i = 0
        right_i = 24
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
    print(encryption_weakness(input_array, encoding_error(input_array)))
