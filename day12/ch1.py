def challenge(arr):
    directions = ['E', 'S', 'W', 'N']
    moves = {d: 0 for d in directions}
    index = 0
    for command in arr:
        direction = directions[index % 4]
        move = command[0]
        step = int(command[1:])
        if move == 'L':
            index -= int(step / 90)
        elif move == 'R':
            index += int(step / 90)
        elif move == 'F':
            moves[direction] += step
        else:
            moves[move] += step
    return (abs(moves['N'] - moves['S']) + abs(moves['E'] - moves['W']))


def from_txt(filepath='input.txt'):
    try:
        array = open(filepath, 'r').read().splitlines()
    except FileNotFoundError:
        filepath = input("Enter full path to input file.\n")
        array = open(filepath, 'r').read().splitlines()
    return array


if __name__ == "__main__":
    input_array = from_txt()
    print(challenge(input_array))
