from queue import PriorityQueue

DIRECTIONS = [
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1],
]

def read_input():
    matrix = []
    file = open("./day-15/input.txt", "r")
    matrix = [[int(char) for char in line.rstrip("\n")] for line in file.readlines()]
    return matrix

class Graph2:
    def __init__(self, matrix):
        self.matrix = matrix
class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight):
        print("u", u)
        self.edges[u][v] = weight
        self.edges[v][u] = weight

def is_in_bounds(matrix, point):
    row, col = point
    if (row >= 0) & (row < len(matrix)) & (col >= 0) & (col < len(matrix[0])):
        return True
    return False

def run():
    matrix = read_input()
    graph = Graph(len(matrix) * len(matrix[0]))

    for row_idx, row in enumerate(matrix):
        for col_idx, val in enumerate(row):
            print("------")
            edge = (row_idx + 1) * (col_idx + 1)
            print("edge", edge)
            for dir in DIRECTIONS:
                next = (row_idx + dir[0], col_idx + dir[1])
                if is_in_bounds(matrix, next):
                    vertex = (next[0] + 1) * (next[1]+1)
                    value = matrix[next[0]][next[1]]
                    graph.add_edge(edge - 1, vertex - 1, value)
    # print(graph.edges)
    # for vert in graph.edges:
    #     print(vert)
    # for row in matrix:
    #     print(row)
    D = dijkstra(graph, 0)
    print(D)


def dijkstra(graph, start_vertex):
    D = {v:float('inf') for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (_, current_vertex) = pq.get()
        graph.visited.append(current_vertex)
        for neighbor in range(graph.v):
            print(current_vertex, graph.edges[current_vertex])
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D

run()
