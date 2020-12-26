def challenge(arr):
    time = int(arr[0])
    buses = arr[1].split(',')
    available = [int(bus) for bus in buses if bus != 'x']
    soonest_buses = {time + bus - time % bus: bus for bus in available}
    soonest_time = min(soonest_buses.keys())
    soonest_bus = soonest_buses[soonest_time]
    return soonest_bus * (soonest_time - time)


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
