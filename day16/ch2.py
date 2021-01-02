import re


def challenge(arr):
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

    n = len(limits)

    possible = [[True for _ in range(n)] for _ in range(n)]

    for ticket in nearby_tickets:
        ticket_valid = True
        for value in ticket:
            valid = False
            for a, b, c, d in limits:
                if any([value in range(a, b + 1), value in range(c, d + 1)]):
                    valid = True
            if not valid:
                ticket_valid = False

        if ticket_valid:
            for i, v in enumerate(ticket):
                for j, (a, b, c, d) in enumerate(limits):
                    if not any([v in range(a, b + 1), v in range(c, d + 1)]):
                        possible[i][j] = False

    mapped = [None] * 20
    used = [False] * 20
    while None in mapped:
        for i in range(20):
            col = [j for j in range(20) if possible[i][j] and not used[j]]
            if len(col) == 1:
                mapped[i] = col[0]
                used[col[0]] = True

    output = 1
    for i, j in enumerate(mapped):
        if j < 6:
            output *= my_ticket[i]
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
