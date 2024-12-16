def get_input(path):
    with open(path, "r") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    return lines

class Tile:
    def __init__(self, chr, x, y, adj_tiles):
        self.chr = chr
        self.pos = Pos(x, y)
        self.adj_tiles = adj_tiles
        self.min_dist_from_start = float("inf")

class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class TileGraph:
    def __init__(self, graph):
        self.graph = []
        for i in range(len(graph)):
            row = []
            for j in range(len(graph)):
                adj_tiles = []
                # TODO: GET ADJ TILES BASED ON THE TYPE
                #       WE WILL NEED SPECIAL LOGIC FOR THE START TILE
                if graph[i][j] == "S":
                    self.start_tile = row[-1]
                    # TODO: FIGURE OUT WHAT KIND OF TILE THE START REALLY IS
                    pass
                elif graph[i][j] == "|":
                    pass
                elif graph[i][j] == "-":
                    pass
                elif graph[i][j] == "7":
                    pass
                elif graph[i][j] == "F":
                    pass
                elif graph[i][j] == "J":
                    pass
                row.append(Tile(graph[i][j], i, j, adj_tiles))

def part1():
    # Construct an adjacency graph based on where you can move
    # from a given tile
    # Traverse the graph to find the furthest tile along the path
    # Note that before we even do that, we should probably filter out tiles that
    # aren't part of the main loop
    # So once we have the loop, we can find the farthest tile
    # Probably have to compute the min number of steps to a given tile
    # using dijkstra's algorithm
    graph = get_input("p10-example1.txt")
    tile_graph = TileGraph(graph)
    start_tile = tile_graph.start_tile


def part2():
    pass

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()
