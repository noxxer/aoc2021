import pathlib
import numpy


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
    low_points = []
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
                low_points.append((row, col))
                risk_level += (1 + curr_height)
                print(f'={curr_height}=', end='')
            else:
                print(f' {curr_height} ', end='')
        print('')

    def extend(area, row, col):
        curr_height = height_map[row][col]
        if row > 0 and height_map[row - 1][col] > curr_height and height_map[row - 1][col] < 9 and (row - 1, col) not in area:
            extend(area, row - 1, col)
            area.append((row - 1, col))
        if row < l1 - 1 and height_map[row + 1][col] > curr_height and height_map[row + 1][col] < 9 and (row + 1, col) not in area:
            area.append((row + 1, col))
            extend(area, row + 1, col)
        if col > 0 and height_map[row][col - 1] > curr_height and height_map[row][col - 1] < 9 and (row, col - 1) not in area:
            area.append((row, col - 1))
            extend(area, row, col - 1)
        if col < l2 - 1 and height_map[row][col + 1] > curr_height and height_map[row][col + 1] < 9 and (row, col + 1) not in area:
            area.append((row, col + 1))
            extend(area, row, col + 1)
    tops = []
    for row, col in low_points:
        area = [(row, col)]
        extend(area, row, col)
        curr_area = len(area)
        tops.append(curr_area)
    top_3 = sorted(tops, reverse=True)[:3]
    return top_3[0] * top_3[1] * top_3[2]
# You guessed 1756


def view_result():
    print(solve())


if __name__ == '__main__':
    view_result()
