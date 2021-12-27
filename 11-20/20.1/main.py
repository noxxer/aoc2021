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


def get_elem(image: list, x, y, default='.'):
    ln = len(image)
    if x < 0 or y < 0 or x >= ln or y >= ln:
        return default
    else:
        return image[x][y]


def enhance_image(image: list, iea: list, default='.') -> list:
    res_image = []
    ln = len(image)

    for x in range(-1, ln + 1):
        line = ''
        for y in range(-1, ln + 1):
            # turning num
            turning_num = ''
            for x_s in range(-1, 2):
                for y_s in range(-1, 2):
                    elem = get_elem(image, x + x_s, y + y_s, default)
                    turning_num = f'{turning_num}{elem}'
            turning_num = int(turning_num.replace('.', '0').replace('#', '1'), 2)
            line += iea[turning_num]
        res_image.append(line.replace('0', '.').replace('1', '#'))
    return res_image


def print_image(image: list):
    lit = 0
    ln = len(image)
    print('')
    for x in range(-1, ln + 1):
        for y in range(-1, ln + 1):
            elem = get_elem(image, x, y)
            if elem == '#':
                lit += 1
            print(end=f'{elem}')
        print('')
    print('')
    return lit


def solve():
    data = get_input()

    row = 0
    iea = ''
    image = []
    for line in data:
        if row == 0:
            iea = list(line.replace('\n', '').replace('.', '0').replace('#', '1'))
        if row > 1:
            img_line = list(line.replace('\n', ''))
            image.append(img_line)
        row += 1

    print('-- Init --')
    print_image(image)

    cnt = 2
    total_lit = 0
    for i in range(cnt):
        if i % 2 == 0 or iea[0] == '.':
            default = '.'
        else:
            default = '#'
        image = enhance_image(image, iea, default)
        print(f'-- {i} --')
        total_lit = print_image(image)

    print('---------------------')
    print(f'Total - {total_lit}')
    return total_lit


# You guessed -


def view_result():
    print(solve())


if __name__ == '__main__':
    view_result()
