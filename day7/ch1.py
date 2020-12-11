def get_rules(input_array):
    all_rules = {}
    for rule in input_array:
        parent, children = rule.split('bags contain')
        parent = parent.strip()
        all_rules[parent] = []
        for ch in children.split(','):
            inside = ch.strip().split(' ')
            all_rules[parent].append(' '.join(inside[1:-1]))
    return all_rules


def whats_in_the_fucking_box(lookup, rules, result):
    for bag, inside in rules.items():
        if lookup in ''.join(inside):
            result.append(bag)
            whats_in_the_fucking_box(bag, rules, result)
    return result


def from_txt(filepath='input.txt'):
    try:
        array = open(filepath, 'r').read().splitlines()
    except FileNotFoundError:
        filepath = input("Enter full path to input file.\n")
        array = open(filepath, 'r').read().splitlines()
    return array


if __name__ == "__main__":
    input_array = from_txt()
    output = []
    rules = get_rules(input_array)
    output += whats_in_the_fucking_box('shiny gold', rules, output)
    print(len(set(output)))
