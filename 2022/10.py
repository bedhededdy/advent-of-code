class CPU:
    def __init__(self):
        self.x = 1
        self.cycles = 0

    def addx(self, v):
        self.x += v
        self.cycles += 2
    
    def noop(self):
        self.cycles += 1

def get_input():
    with open('10.txt', 'r') as f:
        inp_lines = f.read().splitlines()
    return inp_lines

def part1():
    inp_lines = get_input()

    cpu = CPU()
    sig_sum = 0

    for i, line in enumerate(inp_lines):
        instr = line.split(' ')

        if len(instr) == 1:
            cpu.noop()
        else:
            cpu.addx(int(instr[1]))

        # have to do it this retarded way because even if an addx finishes
        # on cycle 20, we are still supposed to use the old value of x
        if (cpu.cycles+1-20) % 40 == 0:
            sig_sum += (cpu.cycles+1) * cpu.x
        elif (cpu.cycles+2-20) % 40 == 0 and inp_lines[i+1] != 'noop':
            sig_sum += (cpu.cycles+2) * cpu.x

    print(sig_sum)

def part2():
    inp_lines = get_input()


    # too much of a pita to deal with the CPU object since
    # it leads to all sorts of problems on the 2 cycles operations
    # since they are handled atomically, when in reality they aren't atomic
    x = 1
    cycles = 0

    for i, line in enumerate(inp_lines):
        instr = line.split(' ')

        if len(instr) == 1:
            if abs(x - cycles%40) <= 1:
                print('#', end='')
            else:
                print('.', end='')

            cycles += 1
            if cycles % 40 == 0:
                print()
        else:
            if abs(x - cycles%40) <= 1:
                print('#', end='')
            else:
                print('.', end='')
            cycles += 1
            if cycles % 40 == 0:
                print()
            if abs(x - cycles%40) <= 1:
                print('#', end='')
            else:
                print('.', end='')
            cycles += 1
            if cycles % 40 == 0:
                print()
            x += int(instr[1])

def main():
    part1()
    part2()

if __name__ == '__main__':
    main()
