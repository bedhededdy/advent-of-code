import math

def get_input(path):
    with open(path, "r") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    return lines

def get_node_map(raw_input):
    node_map = {}
    for line in raw_input[2:]:
        if line == "":
            continue
        node, children = line.split(" = ")
        children = children.translate({ord(c): None for c in "()"})
        left, right = children.split(", ")
        node_map[node] = (left, right)
    return node_map

def part1():
    raw_input = get_input("p8-1.txt")
    sequence = raw_input[0]
    node_map = get_node_map(raw_input)
    steps = 0
    seq_ptr = 0
    node = "AAA"
    while node != "ZZZ":
        dir = sequence[seq_ptr]
        if dir == "L":
            node = node_map[node][0]
        else:
            node = node_map[node][1]
        seq_ptr = (seq_ptr + 1) % len(sequence)
        steps += 1
    print(steps)

def get_z_points(nodes, node_map, sequence):
    z_points = {}
    for node in nodes:
        steps = 0
        seq_ptr = 0
        start = node
        while True:
            dir = sequence[seq_ptr]
            if dir == "L":
                node = node_map[node][0]
            else:
                node = node_map[node][1]
            steps += 1
            seq_ptr = (seq_ptr + 1) % len(sequence)
            if node[-1] == "Z":
                # Something the question fails to mention is that
                # 11A can only hit 11Z and will never hit 12Z
                z_points[start] = steps
                break
    return z_points

def part2():
    raw_input = get_input("p8-1.txt")
    sequence = raw_input[0]
    node_map = get_node_map(raw_input)
    nodes = [node for node in node_map.keys() if node[-1] == "A"]
    z_points = get_z_points(nodes, node_map, sequence)
    vals = list(z_points.values())
    print(math.lcm(*vals))

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()
