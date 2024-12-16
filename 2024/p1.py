from collections import defaultdict

def get_input(fname):
    with open(fname, "r") as f:
        return f.read().split("\n")

def part1():
    lines = get_input("p1-1.txt")
    left_list = []
    right_list = []
    for line in lines:
        if not line: continue
        toks = line.split(" ")
        left_list.append(int(toks[0]))
        right_list.append(int(toks[-1]))
    left_list.sort()
    right_list.sort()
    print(sum([abs(left_list[i] - right_list[i]) for i in range(len(left_list))]))

def part2():
    lines = get_input("p1-1.txt")
    left_list = []
    right_freq_table = defaultdict(int)
    for line in lines:
        if not line: continue
        toks = line.split(" ")
        left_list.append(int(toks[0]))
        right_freq_table[int(toks[-1])] += 1
    print(sum([x * right_freq_table[x] for x in left_list]))

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()
