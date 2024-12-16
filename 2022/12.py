def get_input():
    with open('12.txt', 'r') as f:
        inp_lines = f.read().splitlines()
    return inp_lines

def min_dist(q, dist):
    mn = float('inf')
    x = y = 0
    for coord in q:
        # w/o <= this bugs out
        if dist[coord[0]][coord[1]] <= mn:
            x = coord[0]; y = coord[1]
            mn = dist[x][y]
    return (x, y)

def part1():
    graph = get_input()

    # turn each string into a list of characters
    for row in range(len(graph)):
        graph[row] = list(graph[row])

    source = (20, 0)
    target = (20, 46)

    # fix values for source and end to avoid edge cases
    graph[source[0]][source[1]] = 'a'
    graph[target[0]][target[1]] = 'z'

    # from here this is just dijkstra's algorithm
    dist = [[float('inf') for _ in range(len(graph[0]))] for _ in range(len(graph))]
    dist[source[0]][source[1]] = 0
    prev = [[None for _ in range(len(graph[0]))] for _ in range(len(graph))]

    # TODO: NEED PRIORITY QUEUE THAT CAN HANDLE DYNAMIC DATA, IE THE DIST CHANGES, IN ORDER TO DO EFFICIENTLY
    # QUEUE MUST HAVE DECREMENT PRIORITY FUNCITON
    # RIGHT NOW WE JUST FIND THE MIN BY SEARCHING WHOLE GRAPH EACH TIME
    q = set([(i, j) for i in range(len(graph)) for j in range(len(graph[0]))])
    
    while len(q) > 0:
        u = min_dist(q, dist)
        q.remove(u)

        if u == target:
            break
        else:
            my_letter = ord(graph[u[0]][u[1]])
            neighbors = []

            if u[0] > 0 and (my_letter >= ord(graph[u[0]-1][u[1]]) or my_letter == ord(graph[u[0]-1][u[1]]) - 1):
                neighbors.append((u[0]-1, u[1]))
            if u[0] < len(graph)-1 and (my_letter >= ord(graph[u[0]+1][u[1]]) or my_letter == ord(graph[u[0]+1][u[1]]) - 1):
                neighbors.append((u[0]+1, u[1]))
            if u[1] > 0 and (my_letter >= ord(graph[u[0]][u[1]-1]) or my_letter == ord(graph[u[0]][u[1]-1]) - 1):
                neighbors.append((u[0], u[1]-1))
            if u[1] < len(graph[0])-1 and (my_letter >= ord(graph[u[0]][u[1]+1]) or my_letter == ord(graph[u[0]][u[1]+1]) - 1):
                neighbors.append((u[0], u[1]+1))
            
            for v in neighbors:
                if v in q:
                    alt = dist[u[0]][u[1]] + 1
                    if alt < dist[v[0]][v[1]]:
                        dist[v[0]][v[1]] = alt
                        prev[v[0]][v[1]] = u

    print(dist[target[0]][target[1]])

def part2():
    graph = get_input()

    # turn each string into a list of characters
    for row in range(len(graph)):
        graph[row] = list(graph[row])

    # now we must find shortest path from target to any 'a'
    # so in a sense our target is actually the source
    source = (20, 46)

    # fix values for source and end to avoid edge cases
    graph[source[0]][source[1]] = 'a'
    graph[20][46] = 'z'

    # from here this is just dijkstra's algorithm
    dist = [[float('inf') for _ in range(len(graph[0]))] for _ in range(len(graph))]
    dist[source[0]][source[1]] = 0
    prev = [[None for _ in range(len(graph[0]))] for _ in range(len(graph))]

    # TODO: NEED PRIORITY QUEUE THAT CAN HANDLE DYNAMIC DATA, IE THE DIST CHANGES, IN ORDER TO DO EFFICIENTLY
    # QUEUE MUST HAVE DECREMENT PRIORITY FUNCITON
    # RIGHT NOW WE JUST FIND THE MIN BY SEARCHING WHOLE GRAPH EACH TIME
    q = set([(i, j) for i in range(len(graph)) for j in range(len(graph[0]))])
    
    while len(q) > 0:
        u = min_dist(q, dist)
        q.remove(u)

        my_letter = ord(graph[u[0]][u[1]])
        neighbors = []
        
        # just flip the conditionals from part1
        if u[0] > 0 and (my_letter <= ord(graph[u[0]-1][u[1]]) or my_letter == ord(graph[u[0]-1][u[1]]) + 1):
            neighbors.append((u[0]-1, u[1]))
        if u[0] < len(graph)-1 and (my_letter <= ord(graph[u[0]+1][u[1]]) or my_letter == ord(graph[u[0]+1][u[1]]) + 1):
            neighbors.append((u[0]+1, u[1]))
        if u[1] > 0 and (my_letter <= ord(graph[u[0]][u[1]-1]) or my_letter == ord(graph[u[0]][u[1]-1]) + 1):
            neighbors.append((u[0], u[1]-1))
        if u[1] < len(graph[0])-1 and (my_letter <= ord(graph[u[0]][u[1]+1]) or my_letter == ord(graph[u[0]][u[1]+1]) + 1):
            neighbors.append((u[0], u[1]+1))
        
        for v in neighbors:
            if v in q:
                alt = dist[u[0]][u[1]] + 1
                if alt < dist[v[0]][v[1]]:
                    dist[v[0]][v[1]] = alt
                    prev[v[0]][v[1]] = u

    mn = float('inf')
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 'a' and dist[i][j] < mn:
                mn = dist[i][j]
    print(mn)

def main():
    part1()
    part2()

if __name__ == '__main__':
    main()
