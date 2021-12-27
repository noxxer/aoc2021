import pathlib
from numpy import loadtxt


def get_input():
    script_dir = pathlib.Path(__file__).parent.absolute()
    lines = []
    with open(f'{script_dir}/input.txt') as file:
        while line := file.readline().rstrip():
            lines.append(line)
    return lines


def solve():
    data = get_input()
    gamma_rate = 0
    l = len(data[0])
    gamma = {i: {'0': 0, '1': 0} for i in range(0, l)}
    epsilon_rate = 0
    aim = 0
    for item in data:
        for i in range(0, l):
            char = item[i]
            gamma[i][char] += 1
    gamma_rate_str = ''
    epsilon_rate_str = ''
    for i in range(0, l):
        if gamma[i]['0'] > gamma[i]['1']:
            gamma_rate_str += '0'
            epsilon_rate_str += '1'
        else:
            gamma_rate_str += '1'
            epsilon_rate_str += '0'
    gamma_rate = int(gamma_rate_str, 2)
    epsilon_rate = int(epsilon_rate_str, 2)
    power_consumption = gamma_rate * epsilon_rate
    return power_consumption


def view_result():
    print(solve())


if __name__ == '__main__':
    view_result()
