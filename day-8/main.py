example_input = [
    "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
    "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
    "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
    "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
    "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
    "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
    "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
    "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
    "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
    "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce",
]


ONE_LENGTH = 2
FOUR_LENGTH = 4
SEVEN_LENGTH = 3
EIGHT_LENGTH = 7

ONE_INDEX = 0
FOUR_INDEX = 2
SEVEN_INDEX = 1
EIGHT_INDEX = 9

SIMPLE_INDEXES = [
    ONE_INDEX, 
    FOUR_INDEX, 
    SEVEN_INDEX, 
    EIGHT_INDEX, 
]


SIMPLE_LENGTHS = set([ONE_LENGTH, FOUR_LENGTH, SEVEN_LENGTH, EIGHT_LENGTH])


def read_input():

    file = open("./day-8/input.txt", "r")
    digits = []
    for line in file.read().split("\n"):
        try:
            half_line = line.split(" | ")
            digits.append(( half_line[0].split(" "),half_line[1].split(" ") ) )
        except:
            print("oops")
    file.close()

    # digits = []
    # for line in example_input:
    #     half_line = line.split(" | ")
    #     digits.append(( half_line[0].split(" "),half_line[1].split(" ") ) )

    return digits



# KNOWN: 1,4,7,8

# 2 3 5

# 1 - 2 = 1
# 2 - 1 = 4

# 1 - 3 = 0
# 1 - 5 = 1

# 2 3 5
def add_len_5(pattern_dict, pattern):
    pattern_set = set(pattern)
    # 2
    # 1-2=1
    # 4-2=2
    if compare(pattern_dict, pattern_set, 1, 1) & compare(pattern_dict, pattern_set, 4, 2):
        pattern_dict[2] = pattern_set
        return

    # 3
    # 1-3=0
    elif compare(pattern_dict, pattern_set, 1, 0):
        pattern_dict[3] = pattern_set
        return

    # 5
    # 1-5=1
    # 4-5=1
    elif compare(pattern_dict, pattern_set, 1, 1) & compare(pattern_dict, pattern_set, 4, 1):
        pattern_dict[5] = pattern_set
        return

# 0 6 9
def add_len_6(pattern_dict, pattern):
    pattern_set = set(pattern)
    # 6
    # 4-6=1 <- PROBLEM
    # 1-6=1

    if True & True:
        pass

    if compare(pattern_dict, pattern_set, 4, 1) & compare(pattern_dict, pattern_set, 1, 1):
        pattern_dict[6] = pattern_set

    # 0
    # 4-0=1
    # 1-0=0
    elif (len(pattern_dict[4].difference(pattern_set)) == 1) & (len(pattern_dict[1].difference(pattern_set)) == 0):
        pattern_dict[0] = pattern_set

    # 9
    # 4-9=2
    # 1-9=0
    else:
        pattern_dict[9] = pattern_set

def compare(pattern_dict, pattern_set, number, expected):
    return len(pattern_dict[number].difference(pattern_set)) == expected

def get_pattern_dict(patterns):
    print("------")
    pattern_dict = dict()
    patterns.sort(key=len)

    pattern_dict[1] = set(patterns[ONE_INDEX])
    pattern_dict[4] = set(patterns[FOUR_INDEX])
    pattern_dict[7] = set(patterns[SEVEN_INDEX])
    pattern_dict[8] = set(patterns[EIGHT_INDEX])

    for pattern in patterns:
        if len(pattern) == 6:
            add_len_6(pattern_dict, pattern)
        if len(pattern) == 5:
            add_len_5(pattern_dict, pattern)


    return pattern_dict

def run():
    res = []
    for inputs in read_input():
        output_res = ""
        pattern, output = inputs
        pattern_dict = get_pattern_dict(pattern)

        print(sorted(pattern_dict.keys()))
        for digit in output:
            for key, value in pattern_dict.items():
                if set(digit) == value:
                    output_res += str(key)
        res.append(int(output_res))

    print(sum(res))

run()
