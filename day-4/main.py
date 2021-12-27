day = "day-4"

def read_input(day_folder):
    file = open("./" + day_folder + "/input.txt", "r")
    text = file.read().split("\n\n")
    file.close()
    return text

def check_is_int(item):
    try:
        int(item)
        return True
    except:
        return False

class Board:
    def __init__(self, matrix):
        self.matrix = matrix
        self.numbers_set = set([item for sublist in matrix for item in sublist])
        self.numbers_dict = {}
        self.correct_numbers = []

        for (row_index, row) in enumerate(matrix):
            for (index, num) in enumerate(row):
                self.numbers_dict[num] = (row_index, index)
                
    def handle_number(self, number):
        if number in self.numbers_set:
            self.correct_numbers.append(self.numbers_dict[number])
            self.numbers_set.remove(number)
            self.last_number = number
        return self

    def has_bingo(self):
        rows = [0] * 5
        cols = [0] * 5

        for coords in self.correct_numbers:
            rows[coords[0]] += 1
            if rows[coords[0]] == 5:
                return True

            cols[coords[1]] += 1
            if cols[coords[1]] == 5:
                return True


        return False

    def calculate_score(self):
        print(self.numbers_set, sum(self.numbers_set), self.last_number)
        return sum(self.numbers_set) * self.last_number
        

def make_board(board_input):
    matrix = [[int(num) for num in list(filter(check_is_int, row.split(" ")))] for row in board_input.split("\n")]
    return Board(matrix)

def get_boards(lines):
    boards = []
    for board_input in lines:
        boards.append(make_board(board_input))
    return boards

def run():
    lines = read_input(day)
    numbers = [int(str) for str in lines.pop(0).split(",")]
    boards = get_boards(lines)
    score = 0
    winners = set()

    for num in numbers:
        for (index, board) in enumerate(boards):
            bingo = board.handle_number(num).has_bingo()
            if bingo and index not in winners:
                score = board.calculate_score()
                winners.add(index)

    return score

print(run())
