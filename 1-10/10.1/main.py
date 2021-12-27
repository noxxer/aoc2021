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
    score = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    data = get_input()
    total_score = 0
    for line in data:
        syntax_error_score = 0
        syntax_stack = []
        for ch in line.replace('\n', ''):
            if ch in ['(', '[', '{', '<']:
                syntax_stack.append(ch)
            else:
                check = syntax_stack.pop()
                if f'{check}{ch}' in ['()', '[]', '{}', '<>']:
                    continue
                else:
                    syntax_error_score = score[ch]
        total_score += syntax_error_score

    print(f'Total - {total_score}')
    return total_score


# You guessed 1756


def view_result():
    print(solve())


if __name__ == '__main__':
    view_result()
