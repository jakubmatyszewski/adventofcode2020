import re


def challenge(arr):
    output = 0
    limits = []
    my_ticket = None
    nearby_tickets = []
    for line in arr:
        ints = [int(x) for x in re.findall('\d+', line)]
        if len(ints) == 4:
            limits.append(ints)
        elif len(ints) > 4:
            if my_ticket is None:
                my_ticket = ints
            else:
                nearby_tickets.append(ints)
    for ticket in nearby_tickets:
        for value in ticket:
            valid = False
            for a, b, c, d in limits:
                if any([value in range(a, b + 1), value in range(c, d + 1)]):
                    valid = True
            if not valid:
                output += value
    return output


def from_txt(filepath='input.txt'):
    try:
        array = open(filepath, 'r').readlines()
    except FileNotFoundError:
        filepath = input("Enter full path to input file.\n")
        array = open(filepath, 'r').readlines()
    return array


if __name__ == "__main__":
    input_array = from_txt()
    print(challenge(input_array))
