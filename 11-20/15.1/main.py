import pathlib
from colorama import init, Fore, Back, Style

init()


def get_input():
    script_dir = pathlib.Path(__file__).parent.absolute()
    lines = []
    with open(f'{script_dir}/input.txt') as file:
        for line in file:
            lines.append(line)
    return lines


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
    print('Init')
    total_risk = [[0 for x in range(l_x)] for y in range(l_y)]
    for x in range(l_x):
        for y in range(l_y):
            print(end=f'{chiton_map[x][y]}')
        print('')
    total_risk[0][0] = 0
    # Initialize first row of total risk array
    for x in range(1, l_x):
        total_risk[x][0] = total_risk[x - 1][0] + chiton_map[x][0]

    # Initialize first column of total risk array
    for j in range(1, l_y):
        total_risk[0][j] = total_risk[0][j - 1] + chiton_map[0][j]

    # Construct rest of the total risk array
    for x in range(1, l_x):
        for y in range(1, l_y):
            total_risk[x][y] = min(
                total_risk[x - 1][y],
                total_risk[x][y - 1]
            ) + chiton_map[x][y]
    # path
    print('--- Best path price ---')
    for x in range(l_x):
        for y in range(l_y):
            print(end=f' {str(total_risk[x][y]).zfill(3)} ')
        print('')
    best_risk_level = total_risk[l_x - 1][l_y - 1]
    print(f'Total risk - {best_risk_level}')
    return best_risk_level


# You guessed


def view_result():
    print(solve())


if __name__ == '__main__':
    view_result()
