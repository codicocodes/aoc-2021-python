def read_input(day_folder):
    file = open("./" + day_folder + "/input.txt", "r")
    lines = []
    for line in file:
        lines.append(line)
    file.close()
    return lines

def parse_ints(lines):
    integer_map = map(int, lines)
    return list(integer_map)
