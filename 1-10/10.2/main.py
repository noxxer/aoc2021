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
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }
    score_2 = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4,
    }
    data = get_input()
    total_score = 0
    results =[]
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
                    break
        result = 0
        if syntax_stack and syntax_error_score == 0:
            for i in range(len(syntax_stack)):
                result = result * 5 + score_2[syntax_stack.pop()]
            results.append(result)
            print(f'{result=}')
    results.sort()
    print(results)
    total_score = results[len(results) // 2]
    print(f'Total - {total_score}')
    return total_score

# You guessed 392043


def view_result():
    print(solve())


if __name__ == '__main__':
    view_result()
