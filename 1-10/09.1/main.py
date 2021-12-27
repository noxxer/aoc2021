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
    risk_level = 0
    height_map = []
    row = 0
    for line in data:
        height_map.insert(row, [])
        col = 0
        for point in line.replace('\n', ''):
            height_map[row].insert(col, int(point))
            col += 1
        row += 1
    l1 = len(height_map)
    for row in range(l1):
        l2 = len(height_map[row])
        assert l1 == l2
        for col in range(l2):
            curr_height = height_map[row][col]
            min_round = 10
            if row > 0:
                min_round = min(min_round, height_map[row - 1][col])
            if row < l1 - 1:
                min_round = min(min_round, height_map[row + 1][col])
            if col > 0:
                min_round = min(min_round, height_map[row][col - 1])
            if col < l2 - 1:
                min_round = min(min_round, height_map[row][col + 1])
            if min_round > curr_height:
                risk_level += (1 + curr_height)
                print(end=Fore.RED + f' {curr_height} ' + Style.RESET_ALL)
            else:
                print(end=f' {curr_height} ')
        print('')
    print(f'Total - {risk_level}')
    return risk_level
# You guessed 1756


def view_result():
    print(solve())


if __name__ == '__main__':
    view_result()
