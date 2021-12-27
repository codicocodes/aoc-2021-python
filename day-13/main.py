from collections import namedtuple

Fold = namedtuple('Fold', ['dir', 'val'])

Point = namedtuple('Point', ['x', 'y'])

def read_input():
    file = open("./day-13/input.txt", "r")
    file = file.read()
    dots, folds = file.split("\n\n")
    dots = [[int(coord) for coord in dot.split(",")] for dot in dots.split("\n")]
    dots = [Point(x=coord[0], y = coord[1]) for coord in dots]
    fold_points = [fold.split("=") for fold in folds.split("\n") ]
    fold_points.pop(-1)
    folds = [Fold(dir=point[0][len(point[0])-1], val=int(point[1])) for point in fold_points]
    return (set(dots), folds)

def make_matrix(dots):
    matrix = []
    max_x=0
    max_y=0
    for dot in dots:
        max_x=max(dot.x, max_x)
        max_y=max(dot.y, max_y)
    for idx_y in range(max_y +1):
        row = []
        for _ in range(max_x +1):
            row.append(".")
        matrix.append(row)
    for dot in dots:
        matrix[dot.y][dot.x] = "#"
    return matrix
def run():
    dots, folds = read_input()

    for fold in folds:
        print ("------")
        print(f'dir={fold.dir}')
        print(f'val={fold.val}')
        for dot in dots.copy():
            dots.remove(dot)
            val = getattr(dot, fold.dir)
            diff = abs(val - fold.val)
            val_updated = fold.val - diff if val > fold.val else val
            dot_updated = Point(x=val_updated, y=dot.y) if fold.dir == "x" else Point(x=dot.x, y=val_updated)
            if (dot_updated.x >=0) & (dot_updated.y>=0):
                dots.add(dot_updated)
    matrix = make_matrix(dots)
    for row in matrix:
        print (row)

run()
