import utils

day = "day-3"

def get_most_common_bit(list, index):
    count = 0
    failure= 0
    for bit in list:
        try:
            count += int(bit[index])
        except:
            failure+=1
            pass
    return "1" if count >= len(list) / 2 else "0"


def get_check_index(common, index):
     def check_index(bit):
        return bit[index] == common
     return check_index

def get_co2_rating(lines):
    max_len = len(max(lines, key = len))
    for index in range (0, max_len):
        common = get_most_common_bit(lines, index)
        lines = list(filter(get_check_index(common, index), lines))
        if len(lines)==1:
            break
    return int(lines[0], 2)

def get_oxygen_rating(lines):
    max_len = len(max(lines, key = len))
    for index in range (0, max_len):
        common = get_most_common_bit(lines, index)
        least = "0" if common == "1" else "1"
        lines = list(filter(get_check_index(least, index), lines))
        if len(lines)==1:
            break
    return int(lines[0], 2)

def part_2():
    lines = utils.read_input(day)
    co2 = get_co2_rating(lines)
    oxy = get_oxygen_rating(lines)
    print(co2 * oxy)
    pass

def calculate_epsilon(lines):
    epsilon = ""
    max_len = len(max(lines, key = len))
    for index in range (0, max_len):
        common = get_most_common_bit(lines, index)
        epsilon += "0" if common == "1" else "1"
    return int(epsilon, 2)

def calculate_gamma(lines):
    gamma = ""
    max_len = len(max(lines, key = len))
    for index in range (0, max_len ):
        common = get_most_common_bit(lines, index)
        gamma += common
    return int(gamma, 2)

def part_1():
    lines = utils.read_input(day)
    gamma = calculate_gamma(lines)
    epsilon = calculate_epsilon(lines)
    print(gamma * epsilon)
    pass


# part_1()
part_2()
