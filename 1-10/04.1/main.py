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
    for num in nums:
        just_called = num
        win_nums.append(num)
        for board in boards:
            for row in board:
                if set(row) < set(win_nums):
                    win_board = board
                    break
            else:
                continue
            break
        else:
            continue
        break
    unmarked_sum = 0
    for row in win_board:
        for item in row:
            if item not in win_nums:
                unmarked_sum += int(item)
    score = unmarked_sum * int(just_called)
    return score


def view_result():
    print(solve())


if __name__ == '__main__':
    view_result()
