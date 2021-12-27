import pathlib
from colorama import init, Fore, Back, Style
import networkx as nx

init()


def get_input():
    script_dir = pathlib.Path(__file__).parent.absolute()
    lines = []
    with open(f'{script_dir}/input.txt') as file:
        for line in file:
            lines.append(line)
    return lines


def reduction(value):
    if value > 9:
        return value - 9
    else:
        return value


def find_path(extra_map, x, y):
    max_l = len(extra_map)
    path = [(x, y), ]

    for step in range(10000):
        down_v = 10000
        if y + 1 < max_l:
            down_v = extra_map[x][y + 1]
        right_v = 10000
        if x + 1 < max_l:
            right_v = extra_map[x + 1][y]
        if x < max_l and right_v < down_v:
            x = x + 1
            path.append((x, y))
        elif y < max_l:
            y = y + 1
            path.append((x, y))
        else:
            break
    return path


def solve():
    data = get_input()
    chiton_map = []
    row = 0

    for line in data:
        chiton_map.insert(row, [])
        col = 0
        for point in line.replace('\n', ''):
            chiton_map[row].insert(col, int(point))
            col += 1
        row += 1
    l_y = len(chiton_map)
    l_x = len(chiton_map[0])

    extra_map = []
    for x in range(l_x * 5):
        extra_map.insert(x, [])
        for y in range(l_y * 5):
            extra_map[x].insert(y, 0)

    for x in range(l_x):
        for y in range(l_y):
            value = chiton_map[x][y]
            for x_multi in range(5):
                n_x = x + l_x * x_multi
                for y_multi in range(5):
                    n_y = y + l_y * y_multi
                    n_value = reduction(value + x_multi + y_multi)
                    extra_map[n_x][n_y] = n_value
    l_y = l_y * 5
    l_x = l_x * 5
    print('Init')
    total_risk = [[0 for x in range(l_x)] for y in range(l_y)]
    for x in range(l_x):
        for y in range(l_y):
            print(end=f'{extra_map[x][y]}')
        print('')
    total_risk[0][0] = 0
    # Initialize first row of total risk array
    for x in range(1, l_x):
        total_risk[x][0] = total_risk[x - 1][0] + extra_map[x][0]

    # Initialize first column of total risk array
    for y in range(1, l_y):
        total_risk[0][y] = total_risk[0][y - 1] + extra_map[0][y]

    # Construct rest of the total risk array
    for x in range(1, l_x):
        for y in range(1, l_y):
            total_risk[x][y] = min(
                total_risk[x - 1][y],
                total_risk[x][y - 1]
            ) + extra_map[x][y]
    # step 2 - correct total risk array
    for x in range(l_x - 1, 0, -1):
        for y in range(l_y - 1, 0, -1):
            total_risk[x][y] = min(
                total_risk[x - 1][y],
                total_risk[x][y - 1],
            ) + extra_map[x][y]

    # path
    path = find_path(extra_map, 0, 0)
    print('--- Best path price ---')
    for x in range(l_x):
        for y in range(l_y):
            if (x, y) in path:
                print(end=Fore.LIGHTWHITE_EX + f'{extra_map[x][y]}' + Style.RESET_ALL)
            else:
                print(end=f'{extra_map[x][y]}')

        print('')
    best_risk_level = total_risk[l_x - 1][l_y - 1]
    print(f'Total risk - {best_risk_level}')
    return best_risk_level


# You guessed answer 3012 is too high
# your answer is too low 745


def view_result():
    print(solve())


if __name__ == '__main__':
    view_result()
