import pathlib
from numpy import loadtxt


def get_input():
    script_dir = pathlib.Path(__file__).parent.absolute()
    return loadtxt(f'{script_dir}/input.txt', comments="#", delimiter=",", unpack=False)


def solve():
    data = get_input()
    count = 0
    first = data[0]
    second = data[1]
    third = data[2]
    i = 0
    for item in data:
        if i > 2:
            # last
            l_sum = first + second + third
            log_1 = f'{first}+{second}+{third} = {l_sum}'
            # current
            first = second
            second = third
            third = item
            c_sum = first + second + third
            log_2 = f'{first}+{second}+{third} = {c_sum}'
            if c_sum > l_sum:
                count += 1
                print(f'{log_2} > {log_1}')
            else:
                print('skip')
        i += 1
    return count


def view_result():
    print(solve())


if __name__ == '__main__':
    view_result()
