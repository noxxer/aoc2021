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
    """
          0:      1:      2:      3:      4:
     aaaa    ....    aaaa    aaaa    ....
    b    c  .    c  .    c  .    c  b    c
    b    c  .    c  .    c  .    c  b    c
     ....    ....    dddd    dddd    dddd
    e    f  .    f  e    .  .    f  .    f
    e    f  .    f  e    .  .    f  .    f
     gggg    ....    gggg    gggg    ....

      5:      6:      7:      8:      9:
     aaaa    aaaa    aaaa    aaaa    aaaa
    b    .  b    .  .    c  b    c  b    c
    b    .  b    .  .    c  b    c  b    c
     dddd    dddd    ....    dddd    dddd
    .    f  e    f  .    f  e    f  .    f
    .    f  e    f  .    f  e    f  .    f
     gggg    gggg    ....    gggg    gggg

    """
    know = {
        0: {'count': 6, },
        1: {'count': 2, 'on': 'cf', },  # ! uniq
        2: {'count': 5, },
        3: {'count': 5, },
        4: {'count': 4, },              # ! uniq
        5: {'count': 5, },
        6: {'count': 6, 'off': 'c', },
        7: {'count': 3, },              # ! uniq
        8: {'count': 7, },              # ! uniq
        9: {'count': 6, 'off': 'e', },
    }
    decode = {i for i in range(10)}
    data = get_input()
    count = 0
    for line in data:
        d_data, output = line.replace('\n', '').split('|')
        analysis = {}
        pre_set_counter = {
            1: '',
            4: '',
            7: '',
            8: '',
        }
        pre_set_pattern = []
        for item in d_data.split(' '):
            if item:
                analysis[item] = len(item)
        for key, value in analysis.items():
            if value == 3:
                pre_set_counter[7] = key
                pre_set_pattern.append(set(key))
            elif value == 4:
                pre_set_counter[4] = key
                pre_set_pattern.append(set(key))
            elif value == 2:
                pre_set_counter[1] = key
                pre_set_pattern.append(set(key))
            elif value == 7:
                pre_set_counter[8] = key
                pre_set_pattern.append(set(key))
        line_count = 0
        for item in output.split(' '):
            if item and set(item) in pre_set_pattern:
                line_count += 1
        print(f'{output} - ({line_count})')
        count += line_count
    print(f'Total - {count}')
    return count


def view_result():
    print(solve())


if __name__ == '__main__':
    view_result()
