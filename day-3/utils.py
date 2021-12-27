def read_input(day_folder):
    file = open("./" + day_folder + "/input.txt", "r")
    lines = []
    for line in file:
        lines.append(line.strip())
    file.close()
    return lines

def parse_ints(lines):
    integer_map = map(int, lines)
    return list(integer_map)

def parse_tuples(lines):
    tuples = []
    for line in lines:
        tuples.append(tuple(line.split()))
    return tuples

def binarylist_to_int(str_list):
    return [int(binary_str, 2) for binary_str in str_list]

