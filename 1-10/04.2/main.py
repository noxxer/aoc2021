import pathlib
from numpy import loadtxt


def get_input():
    script_dir = pathlib.Path(__file__).parent.absolute()
    lines = []
    with open(f'{script_dir}/input.txt') as file:
        for line in file:
            lines.append(line)
    return lines


def solve():
    data = get_input()
    nums = data[0].split(',')
    boards = []
    board = []
    for item in data[2:]:
        if item != '\n':
            board.append(item.strip(' ').replace('  ', ' ').replace('\n', '').split(' '))
        else:
            boards.append(board)
            board = []
    boards.append(board)
    win_nums = []
    win_board = None
    just_called = 0
    win_boards = {i: 0 for i in range(0, len(boards))}
    for num in nums:
        just_called = num
        win_nums.append(num)
        i = 0
        for board in boards:
            i += 1
            trans_board = [[] for i in range(0, len(board[0]))]

            for row in board:
                col = 0
                for item in row:
                    trans_board[col].append(item)
                    col += 1
                if set(row) < set(win_nums):
                    win_board = board
                    win_boards[i-1] = 1
                    break
            for col in trans_board:
                if set(col) < set(win_nums):
                    win_board = board
                    win_boards[i-1] = 1
                    break
        already_win = 0
        for i in range(0, len(boards)):
            if win_boards[i]:
                already_win += 1
        if already_win == len(boards):
            break
        if already_win + 1 == len(boards):
            for key, value in win_boards.items():
                if not value:
                    lose_board = boards[key]
    unmarked_sum = 0
    for row in lose_board:
        for item in row:
            if item not in win_nums:
                unmarked_sum += int(item)
    score = unmarked_sum * int(just_called)
    return score


def view_result():
    print(solve())


if __name__ == '__main__':
    view_result()
