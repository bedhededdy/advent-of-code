def get_input():
    with open('13.txt', 'r') as f:
        inp_lines = f.read().splitlines()
    return inp_lines

# -1 is x < y | 1 is x > y | 0 is x == y
def check_order(x, y):
    if isinstance(x, list) and isinstance(y, list):
        for i in range(len(x)):
            if i == len(y):
                break
            res = check_order(x[i], y[i])
            if res != 0:
                return res
        # regardless of whether we broke or got to the end
        # we still get the proper ordering by comparing the lengths
        return (len(x) > len(y)) - (len(x) < len(y))
    elif isinstance(x, list):
        return check_order(x, [y])
    elif isinstance(y, list):
        return check_order([x], y)
    else:
        # equivalent of Java compareTo
        return (x > y) - (x < y)

def part1():
    inp_lines = get_input()

    indices = 0
    pair = 1
    for i in range(0, len(inp_lines), 3):
        x = eval(inp_lines[i])
        y = eval(inp_lines[i+1])
        if check_order(x, y) <= 0:
            indices += pair
        pair += 1

    print(indices)

def part2():
    inp_lines = get_input()
    inp_lines.append('')
    inp_lines.append('[[2]]')
    inp_lines.append('[[6]]')

    eval_lst = []
    for i in range(0, len(inp_lines), 3):
        x = eval(inp_lines[i])
        y = eval(inp_lines[i+1])
        eval_lst.append(x)
        eval_lst.append(y)

    # trivial O(n^2) sort, obviously could do in O(nlgn) if i cared
    for i in range(len(eval_lst)):
        for j in range(i+1, len(eval_lst)):
            if check_order(eval_lst[i], eval_lst[j]) > 0:
                eval_lst[j], eval_lst[i] = eval_lst[i], eval_lst[j]

    res = 1
    for i in range(len(eval_lst)):
        if eval_lst[i] == [[2]] or eval_lst[i] == [[6]]:
            res *= i + 1
    print(res)

def main():
    part1()
    part2()

if __name__ == '__main__':
    main()
