class Cave:
    def __init__(self, id):
        self.id = id
        self.paths = set()

    def get_id(self):
        return self.id

    def add_path(self, cave):
        if cave.get_id() == "start":
            return self
        self.paths.add(cave)
        return self

    def get_paths(self):
        return self.paths

    def print_paths(self):
        print("Paths for: ", self.id ,[cave.get_id() for cave in self.paths])
        pass

def read_input():
    file = open("./day-12/example-input.txt", "r")
    paths = [tuple(line.rstrip("\n").split("-")) for line in file.readlines()]
    caves = {}
    for path in paths:
        start, end =path
        if start not in caves:
            caves[start] = Cave(start)
        if end not in caves:
            caves[end] = Cave(end)
        caves[start].add_path(caves[end])
        caves[end].add_path(caves[start])

    for cave in caves.values():
        cave.print_paths()

    file.close()
    return caves

class Path:
    def __init__(self, small, path):
        self.small = small
        self.path = path

    def clone(self):
        clone = Path(self.small.copy(), self.path.copy())
        return clone

    def can_visit(self, id):
        if "end" in self.path:
            return False

        if id == "end": 
            return True

        return True if id not in self.small else False

    def get_path(self):
        return self.path

    def get_small(self):
        return self.small

    def reached_end(self):
        if len(self.path) == 0:
            return False
        return True if self.path[-1] == "end" else False


    def visit(self, cave):
        id = cave.get_id()
        if self.can_visit(id):
            if id.lower() == id:
                self.small.add(id)
            self.path.append(id)
            return True
        return False


def run():
    caves_dict = read_input()
    start = caves_dict["start"]
    print("run...")

    paths = set() 
    start_path = Path(set(), [])
    visited = start_path.visit(start)
    print("visited start:", visited)
    print("visiting caves now....")

    cheatIds = []
    for id in caves_dict.keys():
        if (id.lower() == id) & (id != "end") & (id != "start"):
            cheatIds.append(id)

    for id in cheatIds:
        cheat = {}
        cheat[id] = False
        print(cheat)
        explore(start, [start.get_id()] , set(), paths, cheat)
    explore(start, [start.get_id()] , set(), paths, {})

    # for id in caves_dict.keys():
    #     cheat = {}
    #     if (id.lower() == id) & (id != "end") & (id != "start"):
    #         cheat[id] = False
    #     print(cheat, "starting here")
    #     explore(start, [start.get_id()] , set(), paths, cheat)
    #     print("Paths Counts", len(paths))
    # for path in paths:
    #     print(path)
    print(len(paths))

def explore(cave, curr, small, paths, special_small):
    print(cave.get_id(), curr, [ next_cave.get_id() for next_cave in cave.get_paths() ])
    for next in cave.get_paths():
        inner_curr = curr.copy()
        inner_small = small.copy()
        inner_special_small = special_small.copy()
        next_id = next.get_id()
        if next_id == "end":
            inner_curr.append(next_id)
            paths.add(tuple(inner_curr))
            continue

        if next_id not in inner_small:
            if next_id.lower() == next_id:
                inner_small.add(next_id)
            inner_curr.append(next_id)
            explore(next, inner_curr.copy(), inner_small.copy(), paths, inner_special_small.copy())
        else:
            inner_val = inner_special_small.get(next_id)
            if inner_val != None:
                if inner_val == False:
                    inner_special_small[next_id] = True
                    print("visiting", next_id, "twice")
                    inner_curr.append(next_id)
                    explore(next, inner_curr.copy(), inner_small.copy(), paths, inner_special_small.copy())

    pass


run()

