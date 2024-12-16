def get_input(fname):
    with open(fname, "r") as f:
        return f.read().split("\n")

def get_middle_elem(lst):
    # Note that we assume that all arrays have an odd number of elements,
    # because the question does not state how to handle arrays with an even
    # number of elements.
    return lst[len(lst) // 2]

def part1():
    lines = get_input("p5-1.txt")

    deps = {}
    sm = 0

    brk_line = None
    for i in range(len(lines)):
        line = lines[i]
        if not line:
            brk_line = i
            break

        dep, pgnum = line.split("|")
        pgnum = int(pgnum)
        dep = int(dep)
        if pgnum not in deps:
            deps[pgnum] = [dep]
        else:
            deps[pgnum].append(dep)

    for i in range(brk_line + 1, len(lines)):
        line = lines[i]
        if not line:
            break

        pages = line.split(",")
        pages = [int(p) for p in pages]

        printed = set()
        pages_set = set(pages)
        correct_order = True
        for i in range(len(pages)):
            page = pages[i]
            if page in deps:
                for dep in deps[page]:
                    if dep not in printed and dep in pages_set:
                        correct_order = False
                        break
            printed.add(page)

        if correct_order:
            sm += get_middle_elem(pages)

    print(sm)

def part2():
    lines = get_input("p5-1.txt")

    deps = {}
    sm = 0

    brk_line = None
    for i in range(len(lines)):
        line = lines[i]
        if not line:
            brk_line = i
            break

        dep, pgnum = line.split("|")
        pgnum = int(pgnum)
        dep = int(dep)
        if pgnum not in deps:
            deps[pgnum] = [dep]
        else:
            deps[pgnum].append(dep)

    for i in range(brk_line + 1, len(lines)):
        line = lines[i]
        if not line:
            break

        pages = line.split(",")
        pages = [int(p) for p in pages]

        printed = set()
        pages_set = set(pages)
        correct_order = True
        for i in range(len(pages)):
            page = pages[i]
            if page in deps:
                for dep in deps[page]:
                    if dep not in printed and dep in pages_set:
                        correct_order = False
                        break
            printed.add(page)

        if correct_order:
            continue

        # You can correctly order the pages via a repeated swapping of elements.
        # Basically, check if the next element is a dependency of the
        # current element. If they are, then swap them. Repeat this
        # until you reach the end of the list of pages. Repeat this loop until
        # no swaps are made. After the nth iteration of the loop,
        # the last n elements of the array will be in the correct position.
        # This approach will even handle
        # redundant dependencies correctly (e.g. a -> b, b -> c, a -> c).
        # Note that there is theoretically more than one correct ordering,
        # but since the question does not specify how to handle such cases,
        # we know that at the very least the middle element will be
        # the same for all correct orderings (or rather that the sum of the
        # middle elements will be the same for any given set of correct
        # orderings across all the improperly ordered prints).
        # The astute observer will note that repeated swapping boils down to
        # the bubble sort algorithm.
        swapped = True
        j = len(pages) - 1
        while swapped:
            swapped = False
            for i in range(j):
                if pages[i] in deps and pages[i + 1] in deps[pages[i]]:
                    pages[i], pages[i + 1] = pages[i + 1], pages[i]
                    swapped = True
            j -= 1

        sm += get_middle_elem(pages)

    print(sm)

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()
