def get_input(fname):
    with open(fname, "r") as f:
        return f.read().split("\n")

def part1():
    lines = get_input("p3-1.txt")
    sm = 0

    for line in lines:
        if not line:
            continue

        last_idx = 0
        while last_idx < len(line):
            last_idx = line.find("mul", last_idx)
            if last_idx == -1:
                break

            last_idx += 3
            if last_idx >= len(line):
                break
            if line[last_idx] != "(":
                continue

            last_idx += 1
            if last_idx >= len(line):
                break

            num1 = ""
            while last_idx < len(line) and line[last_idx].isnumeric():
                num1 += line[last_idx]
                last_idx += 1
            if last_idx >= len(line):
                break
            if num1 == "":
                continue
            num1 = int(num1)

            if line[last_idx] != ",":
                continue
            last_idx += 1
            if last_idx >= len(line):
                break

            num2 = ""
            while last_idx < len(line) and line[last_idx].isnumeric():
                num2 += line[last_idx]
                last_idx += 1
            if last_idx >= len(line):
                break
            if num2 == "":
                continue
            num2 = int(num2)

            if line[last_idx] != ")":
                continue

            sm += num1 * num2
            last_idx += 1

    print(sm)

def parse_potential_do(line, idx):
    idx += 1
    if idx >= len(line):
        return None, idx
    if line[idx] != "o":
        return None, idx

    idx += 1
    if idx >= len(line):
        return None, idx

    if line[idx] == "n":
        idx += 1
        if idx >= len(line):
            return None, idx
        if line[idx] != "'":
            return None, idx
        idx += 1
        if idx >= len(line):
            return None, idx
        if line[idx] != "t":
            return None, idx
        idx += 1
        if idx >= len(line):
            return None, idx
        if line[idx] != "(":
            return None, idx
        idx += 1
        if idx >= len(line):
            return None, idx
        if line[idx] != ")":
            return None, idx
        return "don't", idx + 1
    elif line[idx] == "(":
        idx += 1
        if idx >= len(line):
            return None, idx
        if line[idx] != ")":
            return None, idx
        return "do", idx + 1

def parse_potential_mul(line, idx, enabled):
    idx += 1
    if idx >= len(line):
        return None, idx
    if line[idx] != "u":
        return None, idx

    idx += 1
    if idx >= len(line):
        return None, idx
    if line[idx] != "l":
        return None, idx

    idx += 1
    if idx >= len(line):
        return None, idx
    if line[idx] != "(":
        return None, idx

    idx += 1
    if idx >= len(line):
        return None, idx

    num1 = ""
    while idx < len(line) and line[idx].isnumeric():
        num1 += line[idx]
        idx += 1
    if idx >= len(line):
        return None, idx
    if num1 == "":
        return None, idx
    num1 = int(num1)

    if line[idx] != ",":
        return None, idx
    idx += 1
    if idx >= len(line):
        return None, idx

    num2 = ""
    while idx < len(line) and line[idx].isnumeric():
        num2 += line[idx]
        idx += 1
    if idx >= len(line):
        return None, idx
    if num2 == "":
        return None, idx
    num2 = int(num2)

    if line[idx] != ")":
        return None, idx

    return num1 * num2 if enabled else None, idx + 1

def part2():
    lines = get_input("p3-1.txt")
    sm = 0
    enabled = True

    for line in lines:
        if not line:
            continue

        idx = 0
        while idx < len(line):
            if line[idx] == "m":
                mul_res, idx = parse_potential_mul(line, idx, enabled)
                if mul_res is not None:
                    sm += mul_res
            elif line[idx] == "d":
                do_res, idx = parse_potential_do(line, idx)
                if do_res == "do":
                    enabled = True
                elif do_res == "don't":
                    enabled = False
            else:
                idx += 1

    print(sm)

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()
