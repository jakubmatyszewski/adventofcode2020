def challenge(arr):
    buses = arr[1].split(',')
    buses = [int(bus) if bus != 'x' else 'x' for bus in buses]
    step = [b for b in buses if type(b) is int][0]
    time = 0
    for i, bus in enumerate(buses[1:]):
        i = i + 1
        if type(bus) is int:
            while (time + i) % bus != 0:
                time += step
            step *= bus
    return time


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
