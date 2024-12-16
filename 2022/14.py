def get_input():
    with open('14-test.txt', 'r') as f:
        inp_lines = f.read().splitlines()
    return inp_lines

def flatten(lst):
    ret = ''
    for x in lst:
        ret += x
    return ret

def part1():
    inp_lines = get_input()

    mx_row = 162
    mx_col = 563
    mn_row = 14
    mn_col = 490

    drop_x = 500
    drop_y = 0

    # populate grid with rocks
    grid = [['.' for _ in range(mx_col)] for _ in range(mx_row)]

    for line in inp_lines:
        points = line.split(' -> ')
        for i in range(len(points)):
            points[i] = tuple(map(int, points[i].split(',')))

        for i in range(1, len(points)):
            p0_x, p0_y = points[i-1][0], points[i-1][1]
            p1_x, p1_y = points[i][0], points[i][1]

            if p0_y != p1_y:
                for j in range(min(p0_y, p1_y), max(p0_y, p1_y)+1):
                    grid[j][p0_x] = '#'
            else:
                for j in range(min(p0_x, p1_x), max(p0_x, p1_x)+1):
                    grid[p0_y][j] = '#'
    
    # store highest piece of solid matter in each col in a lookup table
    lookup = {}
    for i in range(mx_col):
        if i < mn_row:
            lookup[i] = -1
        else:
            for j in range(mx_row):
                if grid[j][i] == '#':
                    lookup[i] = j
                    break
            else:
                lookup[i] = -1

    # fill with sand


def part2():
    inp_lines = get_input()

def main():
    part1()
    part2()

if __name__ == '__main__':
    main()
