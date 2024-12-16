def get_input():
    with open('9.txt', 'r') as f:
        inp_lines = f.read().splitlines()
    return inp_lines

def move(h, dir):
    if dir == 'U':
        return (h[0], h[1]+1)
    elif dir == 'D':
        return (h[0], h[1]-1)
    elif dir == 'L':
        return (h[0]-1, h[1])
    else:
        return (h[0]+1, h[1])

def follow(h, t):
    hx = h[0]
    hy = h[1]
    tx = t[0]
    ty = t[1]

    ydiff = hy - ty
    xdiff = hx - tx

    # touching
    if abs(xdiff) <= 1 and abs(ydiff) <= 1:
        return t
    # differ in one plane
    elif xdiff >= 2 and ydiff == 0:
        return (tx+1, ty)
    elif xdiff <= -2 and ydiff == 0:
        return (tx-1, ty)
    elif ydiff >= 2 and xdiff == 0:
        return (tx, ty+1)
    elif ydiff <= -2 and xdiff == 0:
        return (tx, ty-1)
    # differ diagonally
    elif xdiff < 0 and ydiff > 0:
        return (tx-1, ty+1)
    elif xdiff < 0 and ydiff < 0:
        return (tx-1, ty-1)
    elif xdiff > 0 and ydiff > 0:
        return (tx+1, ty+1)
    elif xdiff > 0 and ydiff < 0:
        return (tx+1, ty-1)
    # should be impossible
    else:
        print('PANIC')
        print(h)
        print(t)
        exit(0)
        
def part1():
    inp_lines = get_input()

    h = (0, 0)
    t = (0, 0)

    visited = set()
    visited.add(t)

    for line in inp_lines:
        dir, num = line.split(' ')

        for _ in range(int(num)):
            h = move(h, dir)
            t = follow(h, t)
            visited.add(t)
    
    print(len(visited))

def part2():
    inp_lines = get_input()

    knots = [(0, 0) for _ in range(10)]

    visited = set()
    visited.add((0, 0))

    for line in inp_lines:
        dir, num = line.split(' ')

        for _ in range(int(num)):
            knots[0] = move(knots[0], dir)

            for i in range(1, len(knots)):
                knots[i] = follow(knots[i-1], knots[i])

            visited.add(knots[-1])

    print(len(visited))

def main():
    part1()
    part2()

if __name__ == '__main__':
    main()
