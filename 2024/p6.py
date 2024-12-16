def get_input(fname):
    with open(fname, "r") as f:
        return f.read().split("\n")

def lines_to_matrix(lines):
    matrix = []
    for line in lines:
        if not line:
            continue
        matrix.append(list(line))
    return matrix

def add_to_dict(dictionary, key, value):
    if key in dictionary:
        dictionary[key].append(value)
    else:
        dictionary[key] = [value]

def part1():
    lines = get_input("p6-1.txt")
    matrix = lines_to_matrix(lines)

    obstacles_by_row = {}
    obstacles_by_col = {}
    pos = None
    visited = []

    for row in range(len(matrix)):
        lst = []
        for col in range(len(matrix[0])):
            to_append = False
            if matrix[row][col] == "^":
                pos = (row, col)
                to_append = True
            elif matrix[row][col] == "#":
                add_to_dict(obstacles_by_row, row, col)
                add_to_dict(obstacles_by_col, col, row)
            lst.append(to_append)
        visited.append(lst)

    heading = "N"
    while True:
        if heading == "N":
            while pos[0] >= 0 and matrix[pos[0]][pos[1]] != "#":
                visited[pos[0]][pos[1]] = True
                pos = (pos[0] - 1, pos[1])
            if pos[0] < 0:
                break
            pos = (pos[0] + 1, pos[1])
            heading = "E"
        elif heading == "E":
            while pos[1] < len(matrix[0]) and matrix[pos[0]][pos[1]] != "#":
                visited[pos[0]][pos[1]] = True
                pos = (pos[0], pos[1] + 1)
            if pos[1] >= len(matrix[0]):
                break
            pos = (pos[0], pos[1] - 1)
            heading = "S"
        elif heading == "S":
            while pos[0] < len(matrix) and matrix[pos[0]][pos[1]] != "#":
                visited[pos[0]][pos[1]] = True
                pos = (pos[0] + 1, pos[1])
            if pos[0] >= len(matrix):
                break
            pos = (pos[0] - 1, pos[1])
            heading = "W"
        elif heading == "W":
            while pos[1] >= 0 and matrix[pos[0]][pos[1]] != "#":
                visited[pos[0]][pos[1]] = True
                pos = (pos[0], pos[1] - 1)
            if pos[1] < 0:
                break
            pos = (pos[0], pos[1] + 1)
            heading = "N"

    sm = 0
    for row in range(len(visited)):
        for col in range(len(visited[row])):
            if visited[row][col]:
                sm += 1
    print(sm)

def part2():
    # Figure out what parts of the map are visited by the guard
    # of those locations. We can test those points and the adjacent points
    # to see if putting an obstruction there causes an infinite loop.
    # To test if the guard is in an infinite loop, we can maintain a visited
    # matrix that will tell us if the node has been visitid and the heading of
    # the guard. If the heading is the same and the node has been visited, we
    # have caused the guard to infinite loop. If the guard runs off the map, we
    # have not caused a loop. Note that we only have to test
    # points that are visited by the guard or adjacent to it, because the
    # guard cannot visit any other points (other than new points caused by
    # us placing an obstruction).
    # In the previous step, we determined the guard can visit 5080 unique
    # points, so testing those + adjacent points = 5080 * 4 = 20320 points,
    # which should be computationally feasible. We can probably coalesce
    # ranges of points visited by the guard to skip directly to the next
    # collision or fall off point to optimize the search, but hopefully
    # the simpler approach will be fast enough.
    # If not, we could multithread the search, since each search is independent.
    # Furthermore, we could optimize this by memoizing the list of known
    # positions and heading combinations that produce an infinite loop.
    # In this manner, we can avoid recomputing the same paths over and
    # over again.
    pass

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()
