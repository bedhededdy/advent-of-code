def get_input():
    with open('4.txt', 'r') as f:
        inp_lines = f.read().splitlines()
    return inp_lines

def contains(p1, p2):
    a1, a2 = p1.split('-')
    a1 = int(a1); a2 = int(a2)

    b1, b2 = p2.split('-')
    b1 = int(b1); b2 = int(b2)

    if a1 <= b1 and a2 >= b2:
        return True
    return False

def overlaps(p1, p2):
    a1, a2 = p1.split('-')
    a1 = int(a1); a2 = int(a2)

    b1, b2 = p2.split('-')
    b1 = int(b1); b2 = int(b2)

    if a1 <= b1 and a2 >= b2 or a1 <= b2 and a2 >= b2:
        return True
    return False

def part1():
    inp_lines = get_input()

    ct = 0
    for line in inp_lines:
        p1, p2 = line.split(',')

        if contains(p1, p2) or contains(p2, p1):
            ct += 1
    
    print(ct)

def part2():
    inp_lines = get_input()

    ct = 0
    for line in inp_lines:
        p1, p2 = line.split(',')

        if overlaps(p1, p2) or overlaps(p2, p1):
            ct += 1
    
    print(ct)

# both O(n)
def main():
    part1()
    part2()

if __name__ == '__main__':
    main()
