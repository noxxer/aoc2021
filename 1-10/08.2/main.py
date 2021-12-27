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

    data = get_input()
    count = 0
    for line in data:
        d_data, output = line.replace('\n', '').split('|')
        analysis = {}
        know = {
            0: {'count': 6, 'var': [], },
            1: {'count': 2, 'var': [], },  # ! uniq
            2: {'count': 5, 'var': [], },
            3: {'count': 5, 'var': [], },
            4: {'count': 4, 'var': [], },  # ! uniq
            5: {'count': 5, 'var': [], },
            6: {'count': 6, 'var': [], },
            7: {'count': 3, 'var': [], },  # ! uniq
            8: {'count': 7, 'var': [], },  # ! uniq
            9: {'count': 6, 'var': [], },
        }
        decode = {
            'a': '',
            'b': '',
            'c': '',
            'd': '',
            'e': '',
            'f': '',
            'g': '',
        }
        for item in d_data.split(' '):
            if item:
                l = len(item)
                analysis[item] = l
                for key, value in know.items():
                    if value['count'] == l:
                        value['var'].append(item)
        decode_result = {}
        set_1 = set(know[1]['var'][0])
        set_4 = set(know[4]['var'][0])
        set_7 = set(know[7]['var'][0])
        set_8 = set(know[8]['var'][0])
        # define A
        decode['a'] = list(set(know[7]['var'][0]) - set_1)[0]
        # define 2
        exclude_2 = ''
        for n2 in know[2]['var']:
            if (set_8 - set_4) <= set(n2):
                set_2 = set(n2)
                exclude_2 = n2
                break
        know[2]['var'] = [exclude_2, ]
        know[3]['var'].remove(exclude_2)
        know[5]['var'].remove(exclude_2)
        # define 5
        exclude_5 = ''
        for n5 in know[5]['var']:
            if (set_8 - set_2) <= set(n5):
                set_5 = set(n5)
                exclude_5 = n5
                break
        know[5]['var'] = [exclude_5, ]
        know[3]['var'].remove(exclude_5)
        set_3 = set(know[3]['var'][0])
        # define e
        decode['e'] = list(set_2 - set_3)[0]
        # define b
        decode['b'] = list(set_5 - set_3)[0]
        # define d
        decode['d'] = list(set_4 - set_1 - set(decode['b']))[0]
        for n6 in know[6]['var']:
            if decode['d'] not in n6:
                set_0 = set(n6)
                exclude_0 = n6
            elif decode['e'] in n6:
                set_6 = set(n6)
                exclude_6 = n6
            else:
                set_9 = set(n6)
                exclude_9 = n6
        know[0]['var'] = [exclude_0, ]
        know[6]['var'] = [exclude_6, ]
        know[9]['var'] = [exclude_9, ]

        numb = ''
        for item in output.strip().split(' '):
            if set(item) == set_1:
                numb += '1'
            elif set(item) == set_2:
                numb += '2'
            elif set(item) == set_3:
                numb += '3'
            elif set(item) == set_4:
                numb += '4'
            elif set(item) == set_5:
                numb += '5'
            elif set(item) == set_6:
                numb += '6'
            elif set(item) == set_7:
                numb += '7'
            elif set(item) == set_8:
                numb += '8'
            elif set(item) == set_9:
                numb += '9'
            elif set(item) == set_0:
                numb += '0'
        count += int(numb)
        print(f'{output} - {int(numb)}: total {count}')
    return count


def view_result():
    print(solve())


if __name__ == '__main__':
    view_result()

# 726404 - your answer is too low