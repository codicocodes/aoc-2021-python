import itertools
import collections

Replacement = collections.namedtuple('Replacement', [ "start", "end", "val" ])

def read_input():
    file = open("./day-14/input.txt", "r")
    file = file.read()
    template, rules = file.split("\n\n")
    rules = [tuple(rule.split(" -> ")) for rule in rules.split("\n")]
    rules.pop(-1)
    return (list(template), rules)

def combine_rules(rules, iter):
    combined_rules = itertools.combinations(rules, iter)
    updated_rules = []
    for combined_rule in combined_rules:
        updated_rule = ["", ""]
        for rule in combined_rule:
            updated_rule[0]+=rule[0]
            updated_rule[1] += rule[0][:1] + rule[1] + rule[0][1:]
            updated_rules.append(updated_rule)
    return updated_rules

def stepping(template, rules):
    # print("-------")
    insertions = []
    for rule in rules:
        rule_check = rule[0]
        idx = 0
        # print(rule_check)
        while idx < len(template):
            # print(f"looking for {rule_check} in {template[idx:]}")
            idx = template.find(rule_check, idx)
            if idx == -1: break
            if len(rule_check) > 2:
                print(f"found string with length {len(rule_check)} at idx {idx}")
            # assert(double == template[idx:idx+2])
            idx +=(len(rule_check)- 1)
            replacement = rule[1] + template[idx]
            # print([ idx, replacement ])
            # print(f"inserting {replacement} at {idx} instead of {template[idx]}")
            # if replacement == "NB":
            #     print("------")
            #     print(template)
            #     print(f"found {double} at {idx -1}")
            #     print(f"replacing {template[idx]} with {replacement}")
            #     print("-------")
            insertions.append((idx, replacement))
            # replacement = Replacement(start=idx, end=idx+len(rule[1]), val=rule[1])
            testy = rule[0][0] + rule[1] + rule[0][1]
            print(testy)
            # insertions.append(replacement)
   
    insertions.sort(key=lambda y: y[0], reverse=True)
    list_template = list(template)
    # print(list_template)
    # for insert in insertions:
    #     print(insert)
    # print(template)
    for tup in insertions:
        idx, char = tup
        list_template[idx]=char
        # print("".join(list_template))
    print("INSERTIONS: ", len(insertions))
    template = "".join(list_template)
    return template


def run2(steps):
    template, rules = read_input()
    # rules = combine_rules(rules, 3)
    template = "".join(template)
    for idx in range(steps):
        print(idx)
        template = stepping(template, rules)
        # print(template)
    # print("LENGTH:", len(template))
    res = calculate_res(template)
    print("RES:", res)
    return template

def step(template, rules):
    template_copy = template.copy()
    insertions = []
    # print("--------------")
    for rule in rules:
        prev = ""
        for idx, char in enumerate(template_copy):
            double = prev + char
            if double == rule[0]:
                insertions.append((idx, rule[1] + char))
            prev=char
    insertions.sort(key=lambda y: y[0], reverse=True)
    # for insert in insertions:
    #     print(insert)
    for tup in insertions:
        idx, char = tup
        template[idx]=char
    return list("".join(template))

def calculate_res(template):
    most_common = collections.Counter(template).most_common(1)[0]
    least_common = collections.Counter(template).most_common()[-1]
    return most_common[1] - least_common[1]



# assert(run2(1)=="NCNBCHB")
# assert(run2(2)=="NBCCNBBBCBHCB")
# assert(run(3)=="NBBBCNCCNBBNBNBBCHBHHBCHB")
# assert(run2(3)=="NBBBCNCCNBBNBNBBCHBHHBCHB")
run2(2)
# assert(run2(4)=="NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB")

# run2(3)
# for expect in expects:
#     assert(run2(expect[0])== expect[1])
