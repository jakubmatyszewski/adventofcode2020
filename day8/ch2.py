class Gameboy3000:
    def __init__(self, input_array):
        self.instructions = [i.split(' ') for i in input_array]
        self.reset()

    def reset(self):
        self.accumulator = 0
        self.index = 0
        self.iteration = 0
        self.infinite = False
        self.history = []
        self.suspects = []
        self.examined = []

    def acc(self, instruction):
        self.accumulator += int(instruction[1])
        self.index += 1

    def jmp(self, instruction):
        if self.infinite is True:
            self.examined.append(self.index)
            self.infinite = False
            self.nop(instruction)
        else:
            if self.index not in self.examined:
                self.suspects.append([self.index, self.iteration])
            self.index += int(instruction[1])

    def nop(self, instruction):
        if self.infinite is True:
            self.examined.append(self.index)
            self.infinite = False
            self.jmp(instruction)
        else:
            if self.index not in self.examined:
                self.suspects.append([self.index, self.iteration])
            self.index += 1

    def run(self, bugster=0):
        while self.index != len(self.instructions):
            self.iteration += 1
            self.history.append(self.index)
            instruction = self.instructions[self.index]
            if instruction[0] == 'acc':
                self.acc(instruction)
            elif instruction[0] == 'jmp':
                self.jmp(instruction)
            elif instruction[0] == 'nop':
                self.nop(instruction)
            if self.index in self.history:
                self.infinite = True
                self.index, self.iteration = self.suspects.pop()
                tmp_i = len(self.history)
                self.history = self.history[:self.iteration]
                self.iteration = tmp_i - len(self.history)
                bugger = self.index
        if bugster:
            return self.accumulator
        else:
            return bugger

    def main(self):
        bugster = self.run()
        if self.instructions[bugster][0] == 'jmp':
            self.instructions[bugster][0] = 'nop'
        elif self.instructions[bugster][0] == 'nop':
            self.instructions[bugster][0] = 'jmp'
        self.reset()
        return self.run(bugster)


def from_txt(filepath='input.txt'):
    try:
        array = open(filepath, 'r').read().splitlines()
    except FileNotFoundError:
        filepath = input("Enter full path to input file.\n")
        array = open(filepath, 'r').read().splitlines()
    return array


if __name__ == "__main__":
    input_array = from_txt()
    print(Gameboy3000(input_array).main())
