example_input = [
    "2199943210",
    "3987894921",
    "9856789892",
    "8767896789",
    "9899965678",
]

def read_input():

    file = open("./day-9/input.txt", "r")
    matrix = []
    for line in file.read().split("\n"):
        row = [int(char) for char in line]
        if len(row) != 0:
            matrix.append(row)

    # matrix = []
    # for line in example_input:
    #     matrix.append([int(char) for char in line])

    return matrix

def check_down(matrix, val, row, col):
    if row == len(matrix) - 1:
        return True
    return matrix[row + 1][col] > val

def check_up(matrix, val, row, col):
    if row == 0:
        return True
    return matrix[row - 1][col] > val

def check_left(matrix, val, row, col):
    if col == 0:
        return True
    return matrix[row][col - 1] > val

def check_right(matrix, val, row, col):
    if col == len(matrix[0]) - 1:
        return True
    return matrix[row][col + 1] > val




def copy_matrix(matrix):
    return [row[:] for row in matrix]

def check_lowpoint(matrix, val, row, col):
    return check_up(matrix, val, row, col) & check_down(matrix, val, row, col) & check_left(matrix,val, row, col) & check_right(matrix, val, row, col)

DIRECTIONS = {
    "down": [1, 0],
    "up": [-1, 0],
    "right": [0, 1],
    "left": [0, -1]
}

def is_in_bounds(matrix, point):
    row, col = point
    if (row >= 0) & (row < len(matrix)) & (col >= 0) & (col < len(matrix[0])):
        return True
    return False

def check_basin(matrix, point, dir):
    next_point = (point[0] + DIRECTIONS[dir][0], point[1] + DIRECTIONS[dir][1])
    if(is_in_bounds(matrix, next_point)):
        x,y = next_point
        val = matrix[x][y]
        if val < 9:
            return True
    return False


def add_to_basin(matrix, point, basin):
    basin.add(point)

    if check_basin(matrix, point, "up"):
        next_point = (point[0] + DIRECTIONS["up"][0], point[1] + DIRECTIONS["up"][1])
        if next_point not in basin:
            add_to_basin(matrix, next_point, basin)

    if check_basin(matrix, point, "down"):
        next_point = (point[0] + DIRECTIONS["down"][0], point[1] + DIRECTIONS["down"][1])
        if next_point not in basin:
            add_to_basin(matrix, next_point, basin)

    if check_basin(matrix, point, "left"):
        next_point = (point[0] + DIRECTIONS["left"][0], point[1] + DIRECTIONS["left"][1])
        if next_point not in basin:
            add_to_basin(matrix, next_point, basin)

    if check_basin(matrix, point, "right"):
        next_point = (point[0] + DIRECTIONS["right"][0], point[1] + DIRECTIONS["right"][1])
        if next_point not in basin:
            add_to_basin(matrix, next_point, basin)

    return basin

def calculate_deep_points(matrix):
    deep_points = []
    for row_idx, row in enumerate(matrix):
        for col_idx, val in enumerate(row):
            if check_lowpoint(matrix, val, row_idx, col_idx):
                deep_points.append((row_idx, col_idx))
    return deep_points

def calculate_basins(matrix, deep_points):
    basins = []
    for point in deep_points:
         basin = set()
         add_to_basin(matrix, point, basin)
         basin_size = len(basin)
         basins.append(basin_size)
    return basins

def run():
    matrix = read_input()
    deep_points = calculate_deep_points(matrix)
    basins = calculate_basins(matrix, deep_points)
    biggest_basins = sorted(basins, key=None, reverse=True)[:3]
    res = 1
    for val in biggest_basins:
        res *= val
    print(res)

run()
        


