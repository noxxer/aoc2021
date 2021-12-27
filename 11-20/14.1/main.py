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
    read_rules = False
    insertion_rules = {}
    polymer = ''
    for line in data:
        if line == '\n':
            read_rules = True
            continue
        if read_rules:
            in_template, out_template = line.replace('\n', '').split(' -> ')
            insertion_rules[in_template] = out_template
        else:
            polymer = line.replace('\n', '')

    # init
    step_count = 10
    print('--------init-------')
    print(f'Template:   {polymer}')
    for step in range(step_count):
        new_polymer = ''
        # read pair
        for start in range(len(polymer) - 1):
            element = polymer[start: start + 2]
            new_polymer += f'{element[0]}{insertion_rules[element]}'
        new_polymer += f'{element[1]}'
        print(f'After step {step + 1}:({len(new_polymer)}) - ...')
        polymer = new_polymer
    ch_counter = {}
    for ch in polymer:
        if ch in ch_counter:
            ch_counter[ch] += 1
        else:
            ch_counter[ch] = 1
    ch_sorterd = sorted(ch_counter.items(), key=lambda kv: kv[1])
    return ch_sorterd[-1][1] - ch_sorterd[0][1]


def view_result():
    print(solve())


if __name__ == '__main__':
    view_result()
