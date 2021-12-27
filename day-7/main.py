def read_input():

    file = open("./day-7/input.txt", "r")
    crab_positions = [int(crab_positions) for crab_positions in file.read().split(",")]
    file.close()

    # file = "16,1,2,0,4,2,7,1,2,14"
    # crab_positions = [int(crab_positions) for crab_positions in file.split(",")]

    return crab_positions


def get_fuel(fuel_spend, diff):
    if diff ==0:
        return 0
    if diff == 1:
        return 1
    if diff in fuel_spend:
        return fuel_spend[diff]
    fuel = get_fuel(fuel_spend, diff - 1) + diff
    fuel_spend[diff] = fuel
    return fuel

def run():
    positions = sorted(read_input())
    res = -1

    fuel_spend = {}

    for pos_candidate in range(positions[0], positions[len(positions) - 1] + 1):
        fuel = 0
        for pos in positions:
            diff = abs(pos_candidate - pos)
            fuel += get_fuel(fuel_spend, diff)

        if res >= 0:
            res = min(res, fuel)
        else:
            res = fuel

    print(res)
run()
