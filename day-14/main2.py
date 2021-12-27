import itertools
import collections

Replacement = collections.namedtuple('Replacement', [ "start", "end", "val" ])

def read_input():
    file = open("./day-14/input.txt", "r")
    file = file.read()
    template, rules = file.split("\n\n")
    rules_input = [tuple(rule.split(" -> ")) for rule in rules.split("\n")]
    rules_input.pop(-1)


    return (template, rules_input)



def build_initial_dict(template):
    template_dict = {}
    count = {}
    template = list(template)
    prev = template.pop(0)
    count[prev]=1
    for char in template:
        double = prev + char
        if double in template_dict:
            template_dict[double] += 1
        else:
            template_dict[double]=1

        if char in count:
            count[char] +=1
        else:
            count[char]=1
    return template_dict, count

def run(steps):
    template, rules = read_input()
    template, counts = build_initial_dict(template)

    for idx in range(steps):
        print(idx)
        template = step(template, rules, counts)
        print(template)
    # print(counts)
    print(sum(template.values()))
    print(sum(counts.values()))
    # print(calculate_res(counts))
    # print(sum(template.values()))
    # return template

def calculate_res(template):
    most_common = collections.Counter(template).most_common(1)[0]
    least_common = collections.Counter(template).most_common()[-1]
    return most_common[1] - least_common[1]

def step(template, rules, counts):
    template_copy = template.copy()
    for rule in rules:
        if rule[0] in template:
            if template[rule[0]] > 0:
                print("found one insertion")
                one = rule[0][0] + rule[1]
                two = rule[1] + rule[0][1]
                # print(template)
                # print(f"adding {template[rule[0]]} to count")
                # print("---") 
                # print(rule, "->", one, two)
                # print(sum(counts.values()))
                # print(counts)
                # print(template[rule[0]])
                # print(sum(counts.values()))
                prev = template[rule[0]]
                template_copy[rule[0]] = 0
                if one in template:
                    # print(f"adding {prev} to {rule[0]}")
                    template_copy[one]+=prev
                else:
                    # print(f"setting {prev} to {rule[0]}")
                    template_copy[one]=prev

                if two in template:
                    # print(f"adding {prev} to {rule[0]}")
                    template_copy[two]+=prev
                else:
                    # print(f"setting {prev} to {rule[0]}")
                    template_copy[two]=prev

                # print(f"adding {prev} {rule[1]}")
                if rule[1] in counts:
                    # print(f"started with this many {rule[1]}: {counts[rule[1]]}")
                    counts[rule[1]]+=prev
                else:
                    counts[rule[1]]=prev
    return template_copy

run(2)


