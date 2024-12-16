def get_input():
    with open('8.txt', 'r') as f:
        inp_lines = f.read().splitlines()
    return inp_lines

def trees_visible_left(grid, i, j):
    ct = 1
    orig = j
    while j > 0 and grid[i][orig] > grid[i][j-1]:
        ct += 1
        j -= 1
    if j == 0:
        ct -= 1
    return ct

def trees_visible_right(grid, i, j):
    ct = 1
    orig = j
    while j < len(grid[0])-1 and grid[i][orig] > grid[i][j+1]:
        ct += 1
        j += 1
    if j == len(grid[0])-1:
        ct -= 1
    return ct

def trees_visible_down(grid, i, j):
    ct = 1
    orig = i
    while i < len(grid)-1 and grid[orig][j] > grid[i+1][j]:
        ct += 1
        i += 1
    if i == len(grid)-1:
        ct -= 1
    return ct 

def trees_visible_up(grid, i, j):
    ct = 1
    orig = i
    while i > 0 and grid[orig][j] > grid[i-1][j]:
        ct += 1
        i -= 1
    if i == 0:
        ct -= 1
    return ct

def part1():
    inp_lines = get_input()

    grid = []
    for line in inp_lines:
        tmp = []
        for ch in line:
            tmp.append(int(ch))
        grid.append(tmp)

    # initialize with the number of trees on the edge, since they are obviously visible
    visible = 2*len(grid[0]) + 2*len(grid) - 4

    # do efficiently by storing the size of the tallest tree in each 
    # direction at that point and then just checking against it with a dp matrix
    # just run one scan through the matrix for left down
    # another for right up
    tallest_left = []
    for i in range(len(grid)):
        tallest_left.append([0] * len(grid[0]))

    tallest_up = []
    for i in range(len(grid)):
        tallest_up.append([0] * len(grid[0]))

    # give initial values
    for i in range(len(grid)):
        tallest_left[i][0] = grid[i][0]
    tallest_up[0] = [grid[0][j] for j in range(len(grid[0]))]

    # get calculated values
    for i in range(1, len(grid)):
        for j in range(1, len(grid[i])):
            tallest_left[i][j] = max(tallest_left[i][j-1], grid[i][j])
            tallest_up[i][j] = max(tallest_up[i-1][j], grid[i][j])

    # first row of left and first col of up aren't filled
    for j in range(1, len(grid[0])):
        tallest_left[0][j] = max(tallest_left[0][j-1], grid[0][j])
    for i in range(1, len(grid)):
        tallest_up[i][0] = max(tallest_up[i-1][0], grid[i][0])

    tallest_right = []
    for i in range(len(grid)):
        tallest_right.append([0] * len(grid[0]))

    tallest_down = []
    for i in range(len(grid)):
        tallest_down.append([0] * len(grid[0]))

    # get intial values
    for i in range(len(grid)):
        tallest_right[i][len(grid[0])-1] = grid[i][len(grid[0])-1]
    tallest_down[len(grid[0])-1] = [grid[len(grid[0])-1][j] for j in range(len(grid[0]))]

    # get calculated values
    for i in range(len(grid)-2, -1, -1):
        for j in range(len(grid[i])-2, -1, -1):
            tallest_right[i][j] = max(tallest_right[i][j+1], grid[i][j])
            tallest_down[i][j] = max(tallest_down[i+1][j], grid[i][j])

    # last row of right and last col of up aren't filled
    for j in range(len(grid[0])-2, -1, -1):
        tallest_right[len(grid)-1][j] = max(tallest_right[len(grid)-1][j+1], grid[len(grid)-1][j])
    for i in range(len(grid)-2, -1, -1):
        tallest_down[i][len(grid[0])-1] = max(tallest_down[i+1][len(grid[0])-1], grid[i][len(grid[0])-1])

    # get the number of trees that can be seen from the edge of the grid
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[i])-1):
            if grid[i][j] > tallest_left[i][j-1] or grid[i][j] > tallest_right[i][j+1] or grid[i][j] > tallest_up[i-1][j] or grid[i][j] > tallest_down[i+1][j]:
                visible += 1
    
    print(visible)

def part2():
    inp_lines = get_input()

    grid = []
    for line in inp_lines:
        tmp = []
        for ch in line:
            tmp.append(int(ch))
        grid.append(tmp)

    # NOTE: PROBABLY A DP WAY TO DO THIS EFFICIENTLY LIKE PART1, BUT I HAVEN'T DEDUCED IT

    # get the scenic score for each tree
    mx_score = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            score = trees_visible_left(grid, i, j) * trees_visible_right(grid, i, j) * trees_visible_down(grid, i, j) * trees_visible_up(grid, i, j)
            mx_score = max(mx_score, score)
    print(mx_score)

# Part 1: O(n*m) where n and m are the dimensions of the input matrix
# Part 2: O(n^2 * m^2), but unlikely to happen
def main():
    part1()
    part2()

if __name__ == '__main__':
    main()
