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
    step_count = 40
    print('--------init-------')
    print(f'Template:   {polymer}')
    polymer_map = {}
    for start in range(len(polymer) - 1):
        element = polymer[start: start + 2]
        if element in polymer_map:
            polymer_map[element] += 1
        else:
            polymer_map[element] = 1

    for step in range(step_count):
        new_polymer_map = {}
        # read pair
        for key, count in polymer_map.items():
            new_key_1 = f'{key[0]}{insertion_rules[key]}'
            new_key_2 = f'{insertion_rules[key]}{key[1]}'
            # polymer_map[key] -= 1
            # key_1
            if new_key_1 in new_polymer_map:
                new_polymer_map[new_key_1] += count
            else:
                new_polymer_map[new_key_1] = count
            # key_2
            if new_key_2 in new_polymer_map:
                new_polymer_map[new_key_2] += count
            else:
                new_polymer_map[new_key_2] = count
        polymer_map = new_polymer_map
        print(f'After step {step + 1}: - {polymer_map}')

    ch_counter_ = {}
    for key, count in polymer_map.items():
        for ch in key:
            if ch in ch_counter:
                ch_counter[ch] += count
            else:
                ch_counter[ch] = count
    ch_sorted = sorted(ch_counter.items(), key=lambda kv: kv[1])
    print(f'{ch_sorted=}')
    return (ch_sorted[-1][1] - ch_sorted[0][1]) // 2


def view_result():
    print(solve())

# try 9634526748641
# try 9634526748642
# try 9634526748640 answer is too high
# try 4439442043738
# 4439442043737
# 4439442043739

# ('C', 1511285322328) ('O', 10390169409805)

if __name__ == '__main__':
    view_result()
