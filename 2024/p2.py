def get_input(fname):
    with open(fname, "r") as f:
        return f.read().split("\n")

def all_increasing(line):
    last = line[0]
    for i in range(1, len(line)):
        if last >= line[i]:
            return False
        last = line[i]
    return True

def all_decreasing(line):
    last = line[0]
    for i in range(1, len(line)):
        if last <= line[i]:
            return False
        last = line[i]
    return True

def has_substantial_diff(line):
    prev = line[0]
    for i in range(1, len(line)):
        val = abs(prev - line[i])
        if val < 1 or val > 3:
            return True
        prev = line[i]
    return False

def part1():
    lines = get_input("p2-1.txt")
    sm = 0
    for line in lines:
        if not line:
            continue
        line = [int(x) for x in line.split()]
        if not all_increasing(line) and not all_decreasing(line):
            continue
        if has_substantial_diff(line):
            continue
        sm += 1
    print(sm)

def generate_list_variants(list, removable_indexes):
    variants = []
    if len(removable_indexes) == 0:
        for i in range(len(list)):
            variants.append(list[:i] + list[i+1:])
    else:
        for i in range(len(list)):
            if i in removable_indexes:
                variants.append(list[:i] + list[i+1:])
    return variants

def almost_increasing(line, removable_indexes):
    variants = generate_list_variants(line, removable_indexes)
    for i in range(len(variants)):
        variant = variants[i]
        if all_increasing(variant):
            return True

def almost_decreasing(line, removeable_indexes):
    variants = generate_list_variants(line, removeable_indexes)
    for i in range(len(variants)):
        variant = variants[i]
        if all_decreasing(variant):
            return True

def almost_substantial_diff(line):
    variants = generate_list_variants(line, [])
    removable_indexes = []
    res = True
    for i in range(len(variants)):
        variant = variants[i]
        if not has_substantial_diff(variant):
            removable_indexes.append(i)
            res = False
    if not has_substantial_diff(line):
        removable_indexes.append(None)
        res = False
    return res, removable_indexes

def part2():
    lines = get_input("p2-1.txt")
    sm = 0
    for line in lines:
        if not line:
            continue

        line = [int(x) for x in line.split()]

        res, removable_indexes = almost_substantial_diff(line)
        if res:
            continue

        res = almost_increasing(line, removable_indexes)
        if not res:
            res = almost_decreasing(line, removable_indexes)
            if not res:
                continue

        sm += 1
    print(sm)

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()
