def get_input(path):
    with open(path, "r") as f:
        lines = f.readlines()
        lines = list(filter(lambda x: x != "", [line.strip() for line in lines]))
    return lines

def get_sum(lines):
    sum = 0
    for line in lines:
        for i in range(0, len(line)):
            if line[i].isnumeric():
                first = int(line[i])
                break
        for i in range(len(line)-1, -1, -1):
            if line[i].isnumeric():
                last = int(line[i])
                break
        sum += first * 10 + last
    return sum

def numRepl(numstr, num, line):
    if line == numstr:
        return True
    return False


def replaceStrWithNum(line):
    # Can't do a simple find and replace because
    # eightwothree should be 83 according to the example, meaning that
    # we must do replacements in sliding window fashion
    #
    # To make things worse, there is a missing case in the example
    # eightwo is 82 not 88
    # Frankly, that's bullshit and unacceptable to expect someone
    # to figure out because the edge case is not clarified, especially
    # for a day 1 problem
    #
    # Thankfully, in these digits, there is only one possible character
    # overlap between the end of a number and the beginning of another,
    # so we will just leave the last character in place when we do the replacement
    i = 0
    newline = line
    while i < len(newline):
        if (numRepl("one", 1, newline[i:i+3])):
            newline = newline[:i] + "1" + newline[i+2:]
            i += 1
            continue
        if (numRepl("two", 2, newline[i:i+3])):
            newline = newline[:i] + "2" + newline[i+2:]
            i += 1
            continue
        if (numRepl("three", 3, newline[i:i+5])):
            newline = newline[:i] + "3" + newline[i+4:]
            i += 1
            continue
        if (numRepl("four", 4, newline[i:i+4])):
            newline = newline[:i] + "4" + newline[i+3:]
            i += 1
            continue
        if (numRepl("five", 5, newline[i:i+4])):
            newline = newline[:i] + "5" + newline[i+3:]
            i += 1
            continue
        if (numRepl("six", 6, newline[i:i+3])):
            newline = newline[:i] + "6" + newline[i+2:]
            i += 1
            continue
        if (numRepl("seven", 7, newline[i:i+5])):
            newline = newline[:i] + "7" + newline[i+4:]
            i += 1
            continue
        if (numRepl("eight", 8, newline[i:i+5])):
            newline = newline[:i] + "8" + newline[i+4:]
            i += 1
            continue
        if (numRepl("nine", 9, newline[i:i+4])):
            newline = newline[:i] + "9" + newline[i+3:]
            i += 1
            continue
        i += 1
    return newline


def part1():
    lines = get_input("p1-1.txt")
    print(get_sum(lines))

def part2():
    # Easiest way to do this is to do a pass on the input
    # where we replace all the string instances of the numbers with the actual numbers
    # Then repeat the logic from part 1
    lines = get_input("p1-1.txt")
    lines = [replaceStrWithNum(line) for line in lines]
    print(get_sum(lines))

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()
