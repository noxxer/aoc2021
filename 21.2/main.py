import pathlib
import itertools
from collections import defaultdict
from colorama import init, Fore, Back, Style

init()


def get_input():
    script_dir = pathlib.Path(__file__).parent.absolute()
    lines = []
    with open(f'{script_dir}/input.txt') as file:
        for line in file:
            lines.append(line)
    return lines


class Dice:
    def __init__(self, sided: int):
        self.sided = sided
        self.num = 1

    def get_sum_of(self, n):
        dice_sum = 0
        for i in range(n):
            dice_sum += self.num
            self.num += 1
            if self.num > self.sided:
                self.num = 1
        return dice_sum


def next_pos(pos: int, step: int):
    spaces = 10
    pos = (pos + step) % spaces
    if pos == 0:
        pos = spaces
    return pos


def add_wins(wins, key, count):
    if key in wins:
        wins[key] += count
    else:
        wins[key] = count


def solve():
    # https://adventofcode.com/2021/day/21
    data = get_input()
    player_1_pos = 3
    player_2_pos = 7
    max_score = 21
    # pos_a, score_a, pos_b, score_b, is_step_a
    steps = defaultdict(int)
    steps[(player_1_pos, 0, player_2_pos, 0)] = 1
    wins = {}
    while steps:
        print(f'steps - {len(steps)}')
        curr_step = min(steps, key=lambda i: min(i[1], i[3]))
        count = steps.pop(curr_step)
        for s_1 in itertools.product([1, 2, 3], repeat=3):
            for s_2 in itertools.product([1, 2, 3], repeat=3):
                pos_a = curr_step[0]
                score_a = curr_step[1]
                pos_b = curr_step[2]
                score_b = curr_step[3]
                # player_1
                pos_a = next_pos(pos_a, sum(s_1))
                score_a += pos_a
                if score_a >= max_score:
                    add_wins(wins, (pos_a, score_a, pos_b, score_b), count)
                    break
                # player_2
                pos_b = next_pos(pos_b, sum(s_2))
                score_b += pos_b
                if score_b >= max_score:
                    add_wins(wins, (pos_a, score_a, pos_b, score_b), count)
                    continue
                # push
                steps[(pos_a, score_a, pos_b, score_b)] += count
    p1_count = 0
    p2_count = 0
    for key, value in wins.items():
        if key[1] > 29 or key[3] > 29:
            print(f'{key}: {value}')
        if key[1] >= 21:
            p1_count += value
        else:
            p2_count += value
    result = max(p1_count, p2_count)
    print(f'Total - {p1_count=}, {p2_count=} == {result}')
    return result


# You guessed your answer is too 444356092776315 high


def view_result():
    print(solve())


if __name__ == '__main__':
    view_result()
