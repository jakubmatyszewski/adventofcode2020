def custom_customs(input_array):
    groups = [group.split('\n') for group in input_array]
    s = 0
    for group in groups:
        answers_n = len(group)
        all_answers = ''.join(group)
        counter = {char: 0 for char in set(all_answers)}
        for char in all_answers:
            counter[char] += 1
        s += sum([1 for v in counter.values() if v == answers_n])
    return s


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
