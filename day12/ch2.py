def compute_waypoint(directions):
    north = directions[0] - directions[2]
    east = directions[1] - directions[3]
    return north, east


def challenge(arr):
    directions = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
    pos = [0, 0]
    way_d = [1, 10, 0, 0]
    for command in arr:
        move = command[0]
        step = int(command[1:])
        if move in directions.keys():
            move = directions[command[0]]
            way_d[move] += step
        if move == 'L':
            i = int(step / 90)
            for turn in range(i):
                way_d = way_d[1:] + [way_d[0]]
        elif move == 'R':
            i = int(step / 90)
            for turn in range(i):
                way_d = [way_d[-1]] + way_d[0:-1]
        elif move == 'F':
            waypoint = [i * step for i in compute_waypoint(way_d)]
            pos = [x + y for x, y in zip(pos, waypoint)]
    return sum([abs(i) for i in pos])


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
