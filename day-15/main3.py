from queue import PriorityQueue
import math

def read_input():
    matrix = []
    file = open("./day-15/input.txt", "r")
    matrix = [[int(char) for char in line.rstrip("\n")] for line in file.readlines()]
    return matrix

def get_edge(matrix, pos):
    row_len = len(matrix[0])
    y,x=pos
    return x + (y * row_len)

def get_pos(matrix, edge):
    num_rows = len(matrix)
    y = math.floor(edge/num_rows)
    x = edge % num_rows 
    return (y, x)

def is_in_bounds(matrix, point):
    row, col = point
    if (row >= 0) & (row < len(matrix)) & (col >= 0) & (col < len(matrix[0])):
        return True
    return False


DIRECTIONS = [
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1],
]

# def get_next_starter(prev_tile):
#     next_matrix = []
#     for row in prev_tile:
#         next_row=[]
#         for val in row:
#             next = val+1
#             if next % 10 < next:
#                 next = next - 9
#             next_row.append(next)
#         next_matrix.append(next_row)
#     return next_matrix

def get_next_matrix(tile):
    next_matrix = []
    for row in tile.copy():
        next_row=[]
        for val in row.copy():
            next = val+1
            if next % 10 < next:
                next = next - 9
            next_row.append(next)
        next_matrix.append(next_row)
    return next_matrix

def make_row(tile):
    matrix = []

    for idx in range(len(tile)):
        matrix.append(tile[idx].copy())

    for _ in range(1,5):
        next_tile = get_next_matrix(tile.copy())
        for idx, values in enumerate(next_tile.copy()):
            matrix[idx].extend(values)
    return matrix

def get_starting_tile(tile):
    matrix = []
    for row in tile:
        next_row = []
        for val in row:
            next = val+1
            if next % 10 < next:
                next = next - 9
            next_row.append(next)
        # print(next_row)
    return matrix

# @TODO: Bug at 4564 becoming -> 4, 4, 5, 3
# 4564 seems to be on next row
def build_matrix(tile):
    matrix = []
    next = tile.copy()
    for idx in range(5):
        rows = make_row(next.copy())
        print(next)
        next = get_next_matrix(next)
        # next = get_starting_tile(start)
        print(next)
        print("---")

        # start = [next_start[0][:2], next_start[1][:2]]
        # print(row1)
        # print("---")
        # print(len(row1))
        # print(len(row1[0]))

        for row in rows:
            if len(row) > 0:
                matrix.append(row)
    return matrix

def build_matrix_old(tile):
    nested_matrix = []
    next = tile

    for y in range(0,5):
        prev = next
        next_row=[next]
        for x in range(1,5):
            next = get_next_matrix(next)
            next_row.append(next)
        next = get_next_matrix(prev)
        nested_matrix.append(next_row)

    matrix = nested_matrix
    #     matrix.append(updated_row)

    # for row in matrix:
    #     print("|",row)

    # print(len(matrix))
    # for row in tile:
    #     for val in row:
    #         print(val)
    #         # count=0
    #         for row_idx in range(0,5):
    #             for col_idx in range(0,5):
    #                 pass
    #             pass


    # for idx in range(0,5):
    #     next_row=[]
    #     for idx in range(0,5):
    #         for row in tile:
    #             for val in row:
    #                 next = val+1*idx
    #                 if next % 10 < next:
    #                     next = next - 9
    #                 next_row.append(next)
    #                 # print(row_idx, next)
    #                 pass
    #     print(next_row)
    #     matrix.append(next_row)
        #     pass
    # # print(matrix)
    return matrix

def dijkstra(matrix, pos):
    D = {v:float(math.inf) for v in range(len(matrix[0]) * len(matrix))}
    D[pos] = 0
    pq = PriorityQueue()
    pq.put((0, pos))
    visited = set()

    while not pq.empty():
        _, curr = pq.get()
        visited.add(curr)
        pos = get_pos(matrix, curr)
        y,x=pos
        for dir in DIRECTIONS:
            next = (y + dir[0], x + dir[1])
            if is_in_bounds(matrix, next):
                next_edge = get_edge(matrix, next)
                if next_edge not in visited:
                    distance = matrix[next[0]][next[1]]
                    cost_so_far = D[curr]
                    new_cost = cost_so_far + distance
                    old_cost = D[next_edge]
                    if new_cost < old_cost:
                        pq.put((new_cost, next_edge))
                        D[next_edge] = new_cost

    print(D)

    return D

for row in build_matrix(read_input()):
    print(row)
    pass

# dijkstra(build_matrix(read_input()), 0)
