import pathlib
from numpy import loadtxt


def get_input():
    script_dir = pathlib.Path(__file__).parent.absolute()
    lines = []
    with open(f'{script_dir}/input.txt') as file:
        while (line := file.readline().rstrip()):
            lines.append(line)
    return lines


def solve():
    data = get_input()
    deep = 0
    path = 0
    for item in data:
        direction, value = str(item).split(' ')
        if direction == 'forward':
            path += int(value)
        elif direction == 'down':
            deep += int(value)
        else:
            deep -= int(value)
    return deep * path


def view_result():
    print(solve())


if __name__ == '__main__':
    view_result()
