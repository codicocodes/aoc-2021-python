def read_input():
    file = open("./day-5/input.txt", "r")
    # file = [
    #     "0,9 -> 5,9",
    #     "8,0 -> 0,8",
    #     "9,4 -> 3,4",
    #     "2,2 -> 2,1",
    #     "7,0 -> 7,4",
    #     "6,4 -> 2,0",
    #     "0,9 -> 2,9",
    #     "3,4 -> 1,4",
    #     "0,0 -> 8,8",
    #     "5,5 -> 8,2",
    # ]
    coords = [[[int(coord) for coord in point.split(",")] for point in line.strip().split("->")] for line in file]
    file.close()
    # coords = list(filter(is_vertical_or_horizontal, coords))
    return coords

def is_vertical_or_horizontal(coord):
    start, end = coord
    if start[0] == end[0]:
        return True
    if start[1] == end[1]:
        return True
    return False

def build_matrix(maxes):
    x_max, y_max = maxes
    matrix = []
    for row_index in range(y_max):
        matrix.append([])
        for _ in range(x_max):
            matrix[row_index].append(0)
    return matrix

def find_max(coords):
    x = 0
    y = 0
    for coord in coords:
        start, end = coord
        x = max(x, start[0], end[0])
        y = max(y, start[1], end[1])
    return (x + 1, y + 1)

def fill_coord(matrix, coord):
    first, second = coord
    x_inc = 0 if first[0] == second[0] else 1 if first[0] < second[0] else -1
    y_inc = 0 if first[1] == second[1] else 1 if first[1] < second[1] else -1
    x = first[0]
    y = first[1]

    point_count = max(abs(first[0] - second[0]), abs(first[1] - second[1])) + 1

    for _ in range(point_count):
        matrix[x][y] += 1
        x += x_inc
        y += y_inc
    return matrix

def fill_x_coord(matrix, coord):
        start, end = coord
        times  = 0
        start_range = min(start[0], end[0])
        end_range = max(start[0], end[0]) + 1
        for x in range(start_range, end_range):
            times +=1
            matrix[x][start[1]] += 1
        return matrix

def fill_y_coord(matrix, coord):
        start, end = coord
        times  = 0
        start_range = min(start[1], end[1])
        end_range = max(start[1], end[1]) + 1
        for y in range(start_range, end_range):
            times +=1
            matrix[start[0]][y]+=1
        return matrix

def fill_matrix(matrix, coords):
    for coord in coords: 
        fill_coord(matrix, coord)
    return matrix

def count_intersections(matrix, count): 
    res = 0
    for intersection_count in [item for sublist in matrix for item in sublist]:
        if intersection_count >= count:
            res += 1
    return res

def print_matrix(matrix):
    for row in matrix:
        print(row)

def run():
    coords = read_input()
    maxes = find_max(coords)
    matrix = build_matrix(maxes)
    fill_matrix(matrix, coords)
    print("---")
    # print_matrix(matrix)
    count = count_intersections(matrix, 2)
    print(count)

run()



