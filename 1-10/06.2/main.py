import pathlib
import numpy


def get_input():
    script_dir = pathlib.Path(__file__).parent.absolute()
    lines = []
    with open(f'{script_dir}/input.txt') as file:
        for line in file:
            lines.append(line)
    return lines


def state_sum(state: dict):
    total = 0
    for val in state.values():
        total += val
    return total


def solve():
    data = get_input()
    state = {}
    for age in range(9):
        state[age] = 0
    for n in data[0].split(','):
        state[int(n)] += 1
    sprint = 256
    print(f'i - {state_sum(state)} - {state}')
    for i in range(sprint):
        new_count = state[0]
        # aging
        for age in range(8):
            state[age] = state[age + 1]
        # birth
        state[6] += new_count
        state[8] = new_count
        print(f'{i} - {state_sum(state)} - {state}')
    total = state_sum(state)
    return total

# 255 - 26984457539 - {0: 2376852196, 1: 2731163883, 2: 2897294544, 3: 3164316379, 4: 3541830408, 5: 3681986557, 6: 4275812629, 7: 1985489551, 8: 2329711392}
# 26984457539

def view_result():
    print(solve())


if __name__ == '__main__':
    view_result()
