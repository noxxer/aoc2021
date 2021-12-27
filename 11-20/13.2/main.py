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
    setup_len = 2000
    sign_map = []
    for y in range(setup_len):
        sign_map.insert(y, [])
        for x in range(setup_len):
            sign_map[y].insert(x, ' ')
    folds = []
    read_folds = False
    max_x = 0
    max_y = 0
    for line in data:
        if line == '\n':
            read_folds = True
            continue
        if read_folds:
            fold = line.replace('\n', '').split('fold along ')[1]
            folds.append(fold)
        else:
            x, y = line.replace('\n', '').split(',')
            x, y = int(x), int(y)
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
            sign_map[x][y] = '#'
    # init
    min_x = 0
    min_y = 0
    print('--------init-------')
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if sign_map[x][y] == '#':
                print(end='#')
            else:
                print(end='.')
        print('')
    for fold in folds:
        print('-------------------')
        direction, value = fold.split('=')
        value = int(value)
        # fold 1
        for x in range(max_x + 1):
            for y in range(max_y + 1):
                if direction == 'y' and y >= value:
                    shift = y - value
                    new_y = value - shift
                    if new_y < min_y:
                        min_y = new_y
                    if sign_map[x][new_y] != '#':
                        sign_map[x][new_y] = sign_map[x][y]
                elif direction == 'x' and x >= value:
                    shift = x - value
                    new_x = value - shift
                    if new_x < min_x:
                        min_x = new_x
                    if sign_map[new_x][y] != '#':
                        sign_map[new_x][y] = sign_map[x][y]
        # fold 2
        if direction == 'y':
            max_y = value
        if direction == 'x':
            max_x = value
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if sign_map[x][y] == '#':
                print(end='#')
            else:
                print(end='.')
        print('')
    return 0


def view_result():
    print(solve())


if __name__ == '__main__':
    view_result()
