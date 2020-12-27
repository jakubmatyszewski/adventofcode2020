def challenge(arr):
    arr = list(map(int, arr))
    mem = {e: i for i, e in enumerate(arr, 1)}
    curr = arr[-1]
    for step in range(len(arr), 2020):
        mem[curr], curr = step, 0 if curr not in mem else step - mem[curr]
    return curr


def from_txt(filepath='input.txt'):
    try:
        array = open(filepath, 'r').read()
    except FileNotFoundError:
        filepath = input("Enter full path to input file.\n")
        array = open(filepath, 'r').read()
    return array.split(',')


if __name__ == "__main__":
    input_array = from_txt()
    print(challenge(input_array))
