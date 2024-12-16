shape_to_points = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}

shape_to_lose = {
    'A': 'C',
    'B': 'A',
    'C': 'B'
}

shape_to_win = {
    'C': 'A',
    'A': 'B',
    'B': 'C'
}

def draw(a, b):
    return shape_to_points[a] == shape_to_points[b]

def win(a, b):
    if a == 'A' and b == 'Y':
        return True
    if a == 'B' and b == 'Z':
        return True
    if a == 'C' and b == 'X':
        return True
    return False

def part1():
    with open('2.txt', 'r') as f:
        inp_lines = f.readlines()

    score = 0
    for line in inp_lines:
        opp = line[0]
        rep = line[2]

        if draw(opp, rep):
            score += shape_to_points[rep] + 3
        elif win(opp, rep):
            score += shape_to_points[rep] + 6
        else:
            score += shape_to_points[rep]

    print(score)

def part2():
    with open('2.txt', 'r') as f:
        inp_lines = f.readlines()

    score = 0
    for line in inp_lines:
        opp = line[0]
        rep = line[2]

        if rep == 'X':
            score += shape_to_points[shape_to_lose[opp]]
        elif rep == 'Y':
            score += shape_to_points[opp] + 3
        else:
            score += shape_to_points[shape_to_win[opp]] + 6

    print(score)

# both algorithms are O(n)
def main():
    part1()
    part2()

if __name__ == '__main__':
    main()
