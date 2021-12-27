
def read_input():
    file = open("./day-6/input.txt", "r")
    fish = [int(days_left) for days_left in file.read().split(",")]
    file.close()

    # file = "3,4,3,1,2"
    # fish = [int(days_left) for days_left in file.split(",")]

    return fish

def get_fish_dict(fish_list):
    fish_dict = {} 
    for day in range(9):
        fish_dict[day] = fish_list.count(day)

    return fish_dict

def run_faster():
    days_count = 256
    fish_list = read_input()
    fish_dict = get_fish_dict(fish_list)
    for _ in range(days_count):
        born_fish = 0
        updated_fish_dict = {}
        for day, count in fish_dict.items():
            updated_fish_dict[day - 1] = count
        born_fish = updated_fish_dict[-1]
        del updated_fish_dict[-1]
        updated_fish_dict[6] += born_fish
        updated_fish_dict[8] = born_fish
        fish_dict = updated_fish_dict

    count = 0
    for fish_count in fish_dict.values():
        count += fish_count

    print(count)

run_faster()
