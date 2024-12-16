def get_input():
    # ignore the first 10 lines because they're a bitch to parse
    # i just hardcoded them instead
    with open('5.txt', 'r') as f:
        inp_lines = f.read().splitlines()
    return inp_lines[10:]

def get_init_state():
    s1 = ['B', 'Q', 'C']
    s2 = ['R', 'Q', 'W', 'Z']
    s3 = ['B', 'M', 'R', 'L', 'V']
    s4 = ['C', 'Z', 'H', 'V', 'T', 'W']
    s5 = ['D', 'Z', 'H', 'B', 'N', 'V', 'G']
    s6 = ['H', 'N', 'P', 'C', 'J', 'F', 'V', 'Q']
    s7 = ['D', 'G', 'T', 'R', 'W', 'Z', 'S']
    s8 = ['C', 'G', 'M', 'N', 'B', 'W', 'Z', 'P']
    s9 = ['N', 'J', 'B', 'M', 'W', 'Q', 'F', 'P']

    return [s1, s2, s3, s4, s5, s6, s7, s8, s9]

def part1():
    stacks = get_init_state()
    inp_lines = get_input()

    for line in inp_lines:
        _1, ct, _2, src, _3, dest = line.split(' ')

        for _ in range(int(ct)):
            stacks[int(dest)-1].append(stacks[int(src)-1].pop())

    for stack in stacks:
        print(stack[-1], end='')
    print()

def part2():
    stacks = get_init_state()
    inp_lines = get_input()

    for line in inp_lines:
        _1, ct, _2, src, _3, dest = line.split(' ')

        to_move = []
        for _ in range(int(ct)):
            to_move.append(stacks[int(src)-1].pop())

        while len(to_move) > 0:
            stacks[int(dest)-1].append(to_move.pop())

    for stack in stacks:
        print(stack[-1], end='')
    print()

# both O(n)
def main():
    part1()
    part2()

if __name__ == '__main__':
    main()
