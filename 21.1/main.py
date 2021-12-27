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


def solve():
    # https://adventofcode.com/2021/day/21
    data = get_input()
    player_1_pos = int(data[0].replace('\n', '').split(':')[1])
    player_2_pos = int(data[1].replace('\n', '').split(':')[1])
    max_score = 1000
    total_score_1 = 0
    total_score_2 = 0
    spaces = 10
    game = True
    dice = Dice(100)
    total_rolled = 0
    losing_player_score = 0
    while game:
        # player_1
        step = dice.get_sum_of(3)
        player_1_pos = (player_1_pos + step) % 10
        if player_1_pos == 0:
            player_1_pos = 10
        total_rolled += 3
        total_score_1 += player_1_pos
        print(f'Player 1 rolls {step} and moves to space {player_1_pos} for a total score of {total_score_1}.')
        if total_score_1 >= max_score:
            game = False
            losing_player_score = total_score_2
            continue
        # player_2
        step = dice.get_sum_of(3)
        player_2_pos = (player_2_pos + step) % 10
        if player_2_pos == 0:
            player_2_pos = 10
        total_rolled += 3
        total_score_2 += player_2_pos
        print(f'Player 2 rolls {step} and moves to space {player_2_pos} for a total score of {total_score_2}.')
        if total_score_2 >= max_score:
            game = False
            losing_player_score = total_score_1
            continue
    result = total_rolled * losing_player_score
    print(f'Total - {total_rolled=} * {losing_player_score=} = {result}')
    return result


# You guessed 1756


def view_result():
    print(solve())


if __name__ == '__main__':
    view_result()
