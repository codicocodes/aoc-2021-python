import sys
sys.setrecursionlimit(10000)

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

def is_in_bounds(matrix, point):
    row, col = point
    if (row >= 0) & (row < len(matrix)) & (col >= 0) & (col < len(matrix[0])):
        return True
    return False

def is_end(matrix, pos):
    return (pos[0] == len(matrix) - 1) & (pos[1] == len(matrix[0]) - 1)

# @TODO: Add caching in some way
def dfs(matrix, pos, risk, visited, paths):
    visited = visited.copy()
    visited.add(pos)
    risk += matrix[pos[0]][pos[1]]
    if (len(paths) > 0):
        best = min(paths)
        if risk >= best:
            print(best)
            return
    if is_end(matrix, pos):
        paths.append(risk)
    for dir in DIRECTIONS:
        next = (pos[0] + dir[0], pos[1] + dir[1])
        if next not in visited and is_in_bounds(matrix, next):
            dfs(matrix, next, risk, visited, paths)


def run():
    matrix = read_input()
    start = (0,0)
    risk = 0 - matrix[0][0]
    visited = set()
    paths = []
    dfs(matrix,  start, risk, visited, paths)
    print(min(paths))
    pass

run()
