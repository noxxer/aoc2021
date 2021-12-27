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
    positions = data[0].split(',')
    max_p = 0
    min_p = 0
    for position in positions:
        p = int(position)
        if p > max_p:
            max_p = p
        if p < min_p:
            min_p = p
    optimal_fuel = 100000000000
    for i in range(min_p, max_p):
        fuel = 0
        for position in positions:
            shift = abs(int(position) - i)
            fuel += sum(range(shift + 1))
        if fuel <= optimal_fuel:
            optimal_fuel = fuel
    return optimal_fuel


def view_result():
    print(solve())


if __name__ == '__main__':
    view_result()
