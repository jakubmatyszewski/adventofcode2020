def get_rules(input_array):
    all_rules = {}
    for rule in input_array:
        parent, children = rule.split('bags contain')
        parent = parent.strip()
        all_rules[parent] = []
        for ch in children.split(','):
            inside = ch.strip().split(' ')
            if inside[0].isdigit():
                inp = [' '.join(inside[1:-1])] * int(inside[0])
                all_rules[parent].append(inp)
    return all_rules


class TheBin:
    def __init__(self, lookup='shiny gold'):
        self.count = -1  # We already have initial one.
        self.lookup = lookup
        self.rules = get_rules(input_array)
        self.how_much_is_in_the_bin(self.lookup)

    def how_much_is_in_the_bin(self, bag):
        self.count += 1
        for content in self.rules[bag]:
            for bagg in content:
                self.how_much_is_in_the_bin(bagg)


def from_txt(filepath='input.txt'):
    try:
        array = open(filepath, 'r').read().splitlines()
    except FileNotFoundError:
        filepath = input("Enter full path to input file.\n")
        array = open(filepath, 'r').read().splitlines()
    return array


if __name__ == "__main__":
    input_array = from_txt()
    tb = TheBin()
    print(tb.count)
