import pathlib
from numpy import loadtxt


def get_input():
    script_dir = pathlib.Path(__file__).parent.absolute()
    return loadtxt(f'{script_dir}/input.txt', comments="#", delimiter=",", unpack=False)


def solve():
    data = get_input()
    count = 0
    prev = data[0]
    for item in data:
        if item > prev:
            count += 1
        prev = item
    return count


def view_result():
    print(solve())


if __name__ == '__main__':
    view_result()
