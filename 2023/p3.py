def get_input(path):
    with open(path, "r") as f:
        lines = f.readlines()
        lines = list(filter(lambda x: x != "", [line.strip() for line in lines]))
    return lines

def get_numbers_and_start_pos(line):
    res = []
    i = 0
    while i < len(line):
        if line[i].isdigit():
            start_pos = i
            while i < len(line) and line[i].isdigit():
                i += 1
            end_pos = i
            res.append((int(line[start_pos:end_pos]), start_pos))
        else:
            i += 1
    return res

def is_symbol(ch):
    return ch != "." and not ch.isdigit()

def is_adj_to_symbol(num_start_pos, line_num, schematic):
    i = num_start_pos
    while i < len(schematic[line_num]) and schematic[line_num][i].isdigit():
        # Check the entire square surrounding the digit, with appropriate bounds checking
        for j in range(-1, 2):
            for k in range(-1, 2):
                if line_num + j >= 0 and line_num + j < len(schematic) and i + k >= 0 and i + k < len(schematic[line_num]):
                    if is_symbol(schematic[line_num + j][i + k]):
                        return True
        i += 1
    return False

def get_gear_ratio(line_num, col_num, part_numbers_and_positions, schematic):
    if schematic[line_num][col_num] != "*":
        return 0

    # This could be optimized to not check far away part numbers
    adj_part_numbers = []
    for part_line_num, part_start_pos, part_number in part_numbers_and_positions:
        part_end_pos = part_start_pos + len(str(part_number)) - 1

        # If the part number is within the square surrounding the "*", then add it to the list
        done = False
        for i in range(-1, 2):
            for j in range(-1, 2):
                if line_num + i == part_line_num and col_num + j >= part_start_pos and col_num + j <= part_end_pos:
                    adj_part_numbers.append(part_number)
                    done = True
                    break
            if done:
                break

        if len(adj_part_numbers) > 2:
            break

    if len(adj_part_numbers) == 2:
        return adj_part_numbers[0] * adj_part_numbers[1]
    return 0

def part1():
    schematic = get_input("p3-1.txt")
    sum = 0
    for i in range(len(schematic)):
        numbers_and_start_pos = get_numbers_and_start_pos(schematic[i])
        for number, start_pos in numbers_and_start_pos:
            if is_adj_to_symbol(start_pos, i, schematic):
                sum += number
    print(sum)

def part2():
    schematic = get_input("p3-1.txt")
    sum = 0
    # First we should get all the part numbers and their start positions
    # Next we scan for all "*" characters and just find the ones that
    # are only adjacent to exactly two part numbers
    part_numbers_and_positions = []
    for i in range(len(schematic)):
        numbers_and_start_pos = get_numbers_and_start_pos(schematic[i])
        for number, start_pos in numbers_and_start_pos:
            if is_adj_to_symbol(start_pos, i, schematic):
                part_numbers_and_positions.append((i, start_pos, number))
    for i in range(len(schematic)):
        for j in range(len(schematic[i])):
            sum += get_gear_ratio(i, j, part_numbers_and_positions, schematic)
    print(sum)

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()
