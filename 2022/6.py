def get_input():
    with open('6.txt', 'r') as f:
        inp_lines = f.read().splitlines()
    return inp_lines

def part1():
    inp_lines = get_input()
    inp = inp_lines[0]

    p1 = inp[0]
    p2 = inp[1]
    p3 = inp[2]

    ct = 3
    for i in range(3, len(inp)):
        ct += 1
        ch = inp[i]

        if p1 != p2 and p2 != p3 and p1 != p3 and ch != p1 and ch != p2 and ch != p3:
            print(ct)
            break
        else:
            p1 = p2
            p2 = p3
            p3 = ch


def part2():
    inp_lines = get_input()
    inp = inp_lines[0]

    smm = list(inp[:13])

    ct = 14
    for i in range(14, len(inp)):
        ct += 1
        ch = inp[i]

        if (len(set(smm)) == len(smm)) and (ch not in smm):
            print(ct)
            break
        else:
            for j in range(1, len(smm)):
                smm[j-1] = smm[j]
            smm[12] = ch

# both O(n), but part 2 is done poorly
def main():
    part1()
    part2()

if __name__ == '__main__':
    main()
