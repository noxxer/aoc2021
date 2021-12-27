import pathlib
import numpy


def get_input():
    script_dir = pathlib.Path(__file__).parent.absolute()
    lines = []
    with open(f'{script_dir}/input.txt') as file:
        for line in file:
            lines.append(line)
    return lines


def add_point(space: list, x, y):
    space[x][y] += 1


def line_point(line):
    p1, p2 = line.replace('\n', '').split('->')
    x1, y1 = str(p1).split(',')
    x2, y2 = str(p2).strip().split(',')
    return int(x1), int(y1), int(x2), int(y2)


def solve():
    data = get_input()
    max_x = 0
    max_y = 0
    for line in data:
        x1, y1, x2, y2 = line_point(line)
        if x1 > max_x:
            max_x = x1
        if x2 > max_x:
            max_x = x2
        if y1 > max_y:
            max_y = y1
        if y2 > max_y:
            max_y = y2
    space = numpy.zeros((max_x + 1, max_y + 1))
    for line in data:
        x1, y1, x2, y2 = line_point(line)
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                add_point(space, x1, y)
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                add_point(space, x, y1)
    total = 0
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            if space[x][y] > 1:
                total += 1
    return total


def view_result():
    print(solve())


if __name__ == '__main__':
    view_result()
