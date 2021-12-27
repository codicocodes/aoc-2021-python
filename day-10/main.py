example_input = [
    "[({(<(())[]>[[{[]{<()<>>",
    "[(()[<>])]({[<{<<[]>>(",
    "{([(<{}[<>[]}>{[]{[(<()>",
    "(((({<>}<{<{<>}{[]{[]{}",
    "[[<[([]))<([[{}[[()]]]",
    "[{[{({}]{}}([{[{{{}}([]",
    "{<[[]]>}<{[{[{[]{()[[[]",
    "[<(<(<(<{}))><([]([]()",
    "<{([([[(<>()){}]>(<<{{",
    "<{([{{}}[<[[[<>{}]]]>[]]",
]

def read_input():
    file = open("./day-10/input.txt", "r")
    lines = []
    for line in file.read().split("\n"):
        if len(line) != 0:
            lines.append(line)
    return lines

    # return example_input

CLOSING= {
    "{": "}",
    "[": "]",
    "(": ")",
    "<": ">",
}


ERROR_VALUES= {
    "}": 1197,
    "]": 57,
    ")": 3,
    ">": 25137,
}

COMPLETE_VALUES = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def run():
    lines = read_input()

    errors= {
        "}": 0,
        "]": 0,
        ")": 0,
        ">": 0,
    }

    scores = []
    for line in lines:
        stack = []
        errored = False
        score = 0
        for char in line:
            if char in CLOSING.keys():
                stack.append(char)

            if char in CLOSING.values():

                if len(stack) == 0:
                    errors[char] += 1
                    break

                last = stack.pop(-1)
                if char != CLOSING[last]:
                    errored = True
                    errors[char] += 1
                    break

        if not errored:
            while len(stack) > 0:
                last = stack.pop(-1)
                closing = CLOSING[last]
                score *= 5
                score += COMPLETE_VALUES[closing]
            scores.append(score)

    sorted_scores = sorted(scores)
    middle_idx = int((len(sorted_scores) - 1)/2)
    print(sorted_scores[middle_idx])

run()

