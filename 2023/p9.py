def get_input(path):
    with open(path, "r") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    return lines

def is_all_zero(row):
    for val in row:
        if val != 0:
            return False
    return True

def part1():
    histories = get_input("p9-1.txt")
    ext_val_sum = 0
    for history in histories:
        if history == "":
            continue
        val_tbl = [[int(val) for val in history.split(" ")]]
        row = 0
        while not is_all_zero(val_tbl[row]):
            new_row = [0] * (len(val_tbl[row]) - 1)
            for i in range(len(new_row)):
                new_row[i] = val_tbl[row][i+1] - val_tbl[row][i]
            row = row + 1
            val_tbl.append(new_row)
        ext_val = 0
        for i in range(row, -1, -1):
            ext_val = ext_val + val_tbl[i][len(val_tbl[i])-1]
        ext_val_sum += ext_val
    print(ext_val_sum)

def part2():
    histories = get_input("p9-1.txt")
    ext_val_sum = 0
    for history in histories:
        if history == "":
            continue
        val_tbl = [[int(val) for val in history.split(" ")]]
        row = 0
        while not is_all_zero(val_tbl[row]):
            new_row = [0] * (len(val_tbl[row]) - 1)
            for i in range(len(new_row)):
                new_row[i] = val_tbl[row][i+1] - val_tbl[row][i]
            row = row + 1
            val_tbl.append(new_row)
        ext_val = 0
        for i in range(row, -1, -1):
            ext_val = val_tbl[i][0] - ext_val
        ext_val_sum += ext_val
    print(ext_val_sum)


def main():
    part1()
    part2()

if __name__ == "__main__":
    main()
