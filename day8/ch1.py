def get_rules(input_array):
    accumulator = 0
    instructions = [i.split(' ') for i in input_array]
    infinite = False
    index = 0
    history = [0]
    while infinite is not True:
        history.append(index)
        instruction = instructions[index]
        if instruction[0] == 'acc':
            accumulator += int(instruction[1])
            index += 1
        elif instruction[0] == 'jmp':
            index += int(instruction[1])
        elif instruction[0] == 'nop':
            index += 1
        if index in history:
            infinite = True
    return accumulator


def from_txt(filepath='input.txt'):
    try:
        array = open(filepath, 'r').read().splitlines()
    except FileNotFoundError:
        filepath = input("Enter full path to input file.\n")
        array = open(filepath, 'r').read().splitlines()
    return array


if __name__ == "__main__":
    input_array = from_txt()
    print(get_rules(input_array))
