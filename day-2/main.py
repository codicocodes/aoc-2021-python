import utils

day = "day-2"

def part_1():
    commands = utils.parse_tuples(utils.read_input(day))
    horizontal = 0
    depth = 0
    for command in commands:
        match command[0]:
            case "up":
                depth -= int(command[1])
            case "down":
                depth += int(command[1])
            case "forward":
                horizontal += int(command[1])

    print(horizontal * depth)
    pass

def part_2():
    commands = utils.parse_tuples(utils.read_input(day))
    horizontal = 0
    depth = 0
    aim = 0
    for command in commands:
        match command[0]:
            case "up":
                aim -= int(command[1])
            case "down":
                aim += int(command[1])
            case "forward":
                horizontal += int(command[1])
                depth += int(command[1]) * aim

    print(horizontal * depth)
    pass

part_2()
