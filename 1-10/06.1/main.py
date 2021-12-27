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
    state = {}
    for n in data[0].split(','):
        if int(n) in state:
            state[int(n)] += 1
        else:
            state[int(n)] = 1
    sprint = 256
    for i in range(sprint):


        print(f'{i} - {population}')
        new_count = 0
        for fish in range(population):
            fish_state = state[fish]
            if fish_state == 0:
                state[fish] = 6
                new_count += 1
            else:
                state[fish] = fish_state - 1
        for n in range(new_count):
            state.append(8)
    total = len(state)
    return total


def view_result():
    print(solve())


if __name__ == '__main__':
    view_result()
