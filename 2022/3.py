def get_input():
    with open('3.txt', 'r') as f:
        # avoids adding the \n like f.readlines()
        inp_lines = f.read().splitlines()
    return inp_lines

def get_priority(a):
    if a >= 'a' and a <= 'z':
        return ord(a) - ord('a') + 1
    return ord(a) - ord('A') + 27

def part1():
    inp_lines = get_input()

    sm = 0
    for line in inp_lines:
        h1 = set(line[:len(line)//2])
        h2 = set(line[len(line)//2:])

        sm += get_priority(list(h1.intersection(h2))[0])

    print(sm)


def part2():
    inp_lines = get_input()

    sm = 0
    for i in range(0, len(inp_lines), 3):
        h1 = set(inp_lines[i])
        h2 = set(inp_lines[i+1])
        h3 = set(inp_lines[i+2])

        sm += get_priority(list(h1.intersection(h2).intersection(h3))[0])
    
    print(sm)

# both O(n)
def main():
    part1()
    part2()

if __name__ == '__main__':
    main()
