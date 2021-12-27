def read_input():
    file = open("./day-11/input.txt", "r")
    matrix = [[int(char) for char in line.rstrip("\n")] for line in file.readlines()]
    file.close()
    return matrix

DIRECTIONS = [
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1],
    [1, 1],
    [-1, -1],
    [-1, 1],
    [1, -1],
]

def is_in_bounds(matrix, point):
    row, col = point
    if (row >= 0) & (row < len(matrix)) & (col >= 0) & (col < len(matrix[0])):
        return True
    return False

def handle_flash(matrix, point, flashes):
    for dir in DIRECTIONS:
        next_point = (point[0] + dir[0], point[1] + dir[1])
        if is_in_bounds(matrix, next_point):
            if next_point not in flashes:
                x,y = next_point
                val = matrix[x][y] + 1
                matrix[x][y] = val
                if val > 9:
                    matrix[x][y] = 0
                    flashes.add(next_point)
                    handle_flash(matrix, next_point, flashes)


def run():
    steps = 20000
    matrix = read_input()

    total_flashes = 0
    for step in range(steps):
        flashes = set()
        for x,row in enumerate(matrix):
            for y,oct in enumerate(row):
                oct = oct+1
                matrix[x][y] = oct
                if oct > 9:
                    flashes.add((x,y))
                    matrix[x][y] = 0

        for flash in list(flashes):
            handle_flash(matrix, flash, flashes)
        total_flashes += len(flashes)
        if len(flashes) == len(matrix) * len(matrix[0]):
            # PART 2
            print("STEP", step)
            break
run()
