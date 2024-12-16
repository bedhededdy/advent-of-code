import heapq

def part1():
    # O(n)
    with open('1.txt', 'r') as f:
        inp_lines = f.readlines()

    mx = 0
    curr = 0
    for line in inp_lines:
        if line == '\n':
            mx = max(mx, curr)
            curr = 0
        else:
            curr += int(line)

    print(mx)

def part2():
    # O(n) by converting to max heap at end
    with open('1.txt', 'r') as f:
        inp_lines = f.readlines()

    lst = []
    curr = 0
    for line in inp_lines:
        if line == '\n':
            lst.append(curr)
            curr = 0
        else:
            curr += int(line)

    print(sum(heapq.nlargest(3, lst)))

def main():
    part1()
    part2()

if __name__ == '__main__':
    main()
