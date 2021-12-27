import collections

def read_input():
    file = open("./day-14/input.txt", "r")
    file = file.read()
    template, rules = file.split("\n\n")
    rules_input = [tuple(rule.split(" -> ")) for rule in rules.split("\n")]
    rules_input.pop(-1)
    rules = {}
    for rule in rules_input:
        input,output = rule
        rules[input] = output
    return (build_pairs(template), rules, build_elements(template))

def build_pairs(template):
    pairs = {}
    template = list(template)
    prev = template.pop(0)
    for char in template:
        double = prev + char
        if double in pairs:
            pairs[double] += 1
        else:
            pairs[double]=1
        prev = char
    return pairs

def build_elements(template):
    elements = {}
    for char in template:
        if char in elements:
            elements[char] +=1
        else:
            elements[char]=1
    return elements

def step(pairs, rules, elements):
    for pair, pair_count in pairs.copy().items():
        char = rules.get(pair)
        if char:
            one = pair[0] + char
            two = char + pair[1]

            if char not in elements:
                elements[char] = 0
            if one not in pairs:
                pairs[one] = 0
            if two not in pairs:
                pairs[two] = 0

            elements[char] +=pair_count
            pairs[pair] -= pair_count
            pairs[one] += pair_count
            pairs[two] += pair_count

def run(steps):
    pairs, formula, elements = read_input()
    for _ in range(steps):
        step(pairs, formula, elements)
    most_common = collections.Counter(elements).most_common(1)[0]
    least_common = collections.Counter(elements).most_common()[-1]
    print(most_common[1] - least_common[1])

run(40)
