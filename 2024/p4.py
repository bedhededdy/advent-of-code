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

def get_dimensions(matrix):
    return len(matrix[0]), len(matrix)

def check_diagonal(matrix, i, j):
    ltr_down, ltr_up, rtl_down, rtl_up = True, True, True, True
    w, h = get_dimensions(matrix)

    if i + 3 < w and j + 3 < h:
        if matrix[i + 1][j + 1] != "M":
            ltr_down = False
        if ltr_down and matrix[i + 2][j + 2] != "A":
            ltr_down = False
        if ltr_down and matrix[i + 3][j + 3] != "S":
            ltr_down = False
    else:
        ltr_down = False

    if i + 3 < w and j - 3 >= 0:
        if matrix[i + 1][j - 1] != "M":
            ltr_up = False
        if ltr_up and matrix[i + 2][j - 2] != "A":
            ltr_up = False
        if ltr_up and matrix[i + 3][j - 3] != "S":
            ltr_up = False
    else:
        ltr_up = False

    if i - 3 >= 0 and j - 3 >= 0:
        if matrix[i - 1][j - 1] != "M":
            rtl_up = False
        if rtl_up and matrix[i - 2][j - 2] != "A":
            rtl_up = False
        if rtl_up and matrix[i - 3][j - 3] != "S":
            rtl_up = False
    else:
        rtl_up = False

    if i - 3 >= 0 and j + 3 < h:
        if matrix[i - 1][j + 1] != "M":
            rtl_down = False
        if rtl_down and matrix[i - 2][j + 2] != "A":
            rtl_down = False
        if rtl_down and matrix[i - 3][j + 3] != "S":
            rtl_down = False
    else:
        rtl_down = False

    return int(ltr_down) + int(ltr_up) + int(rtl_down) + int(rtl_up)

def check_vertical(matrix, i, j):
    forward, backward = True, True
    w, h = get_dimensions(matrix)

    if i + 3 < w:
        if matrix[i + 1][j] != "M":
            forward = False
        if forward and matrix[i + 2][j] != "A":
            forward = False
        if forward and matrix[i + 3][j] != "S":
            forward = False
    else:
        forward = False

    if i - 3 >= 0:
        if matrix[i - 1][j] != "M":
            backward = False
        if backward and matrix[i - 2][j] != "A":
            backward = False
        if backward and matrix[i - 3][j] != "S":
            backward = False
    else:
        backward = False

    return int(forward) + int(backward)

def check_horizontal(matrix, i, j):
    forward, backward = True, True
    w, h = get_dimensions(matrix)

    if j + 3 < h:
        if matrix[i][j + 1] != "M":
            forward = False
        if forward and matrix[i][j + 2] != "A":
            forward = False
        if forward and matrix[i][j + 3] != "S":
            forward = False
    else:
        forward = False

    if j - 3 >= 0:
        if matrix[i][j - 1] != "M":
            backward = False
        if backward and matrix[i][j - 2] != "A":
            backward = False
        if backward and matrix[i][j - 3] != "S":
            backward = False
    else:
        backward = False

    return int(forward) + int(backward)

def part1():
    lines = get_input("p4-1.txt")
    matrix = lines_to_matrix(lines)
    sm = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != "X":
                continue
            diag = check_diagonal(matrix, i, j)
            horz = check_horizontal(matrix, i, j)
            vert = check_vertical(matrix, i, j)
            sm += diag + horz + vert
    print(sm)

def makes_cross(matrix, i, j):
    w, h = get_dimensions(matrix)

    if not (i + 2 < w) or not (j + 2 < h):
        return False

    tlm, tls, trm, trs = False, False, False, False

    if matrix[i][j] == "M":
        tlm = True
    if matrix[i][j] == "S":
        tls = True
    if matrix[i][j + 2] == "M":
        trm = True
    if matrix[i][j + 2] == "S":
        trs = True

    if not (tlm or tls) or not (trm or trs):
        return False
    if matrix[i + 1][j + 1] != "A":
        return False

    if tlm and not matrix[i + 2][j + 2] == "S":
        return False
    if tls and not matrix[i + 2][j + 2] == "M":
        return False
    if trm and not matrix[i + 2][j] == "S":
        return False
    if trs and not matrix[i + 2][j] == "M":
        return False

    return True

def part2():
    lines = get_input("p4-1.txt")
    matrix = lines_to_matrix(lines)
    sm = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not makes_cross(matrix, i, j):
                continue
            sm += 1
    print(sm)

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()
