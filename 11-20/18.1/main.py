import pathlib
import pprint
from typing import Optional, Union
import json
from colorama import init, Fore, Back, Style

init()


def get_input():
    script_dir = pathlib.Path(__file__).parent.absolute()
    lines = []
    with open(f'{script_dir}/input.txt') as file:
        for line in file:
            lines.append(line)
    return lines


class FishNum:

    def __str__(self):
        # return f'{self.level}: [{self.a}, {self.b}]'
        return f'[{self.a}, {self.b}]'

    @classmethod
    def from_list(cls, values: list, level=0):
        a = values[0]
        b = values[1]
        if isinstance(a, int):
            a = a
        else:
            a = cls.from_list(a, level+1)
        if isinstance(b, int):
            b = b
        else:
            b = cls.from_list(b, level+1)
        return cls(a, b, level)

    def explode(self) -> bool:
        is_explode = False
        if isinstance(self.a, FishNum):
            is_explode |= self.a.explode()
            if self.a.is_explode:
                self.add_left = self.a.a
                self.add_b_side(self.a.b)
                self.a = 0
        if isinstance(self.b, FishNum) and not is_explode:
            is_explode |= self.b.explode()
            if self.b.is_explode:
                self.add_right = self.b.b
                self.add_a_side(self.b.a)
                # self.a += self.b.a
                self.b = 0
        if self.level > 3 and not is_explode:
            is_explode = True
            self.is_explode = True
        # explosion wave
        if isinstance(self.a, FishNum):
            if self.a.add_right > 0:
                self.add_b_side(self.a.add_right)
                self.a.add_right = 0
            if self.a.add_left > 0:
                self.add_left = self.a.add_left
                self.a.add_left = 0
        if isinstance(self.b, FishNum):
            if self.b.add_left > 0:
                self.add_a_side(self.b.add_left)
                self.b.add_left = 0
            if self.b.add_right > 0:
                self.add_right = self.b.add_right
                self.b.add_right = 0
        return is_explode

    def split(self) -> bool:
        is_split = False
        # a
        if isinstance(self.a, int) and self.a > 9:
            is_split = True
            self.a = FishNum(self.a // 2, self.a - (self.a // 2), level=self.level + 1)
            return is_split
        elif isinstance(self.a, FishNum):
            is_split |= self.a.split()
        # stop iteration
        if is_split:
            return is_split
        # b
        if isinstance(self.b, int) and self.b > 9:
            is_split = True
            self.b = FishNum(self.b // 2, self.b - (self.b // 2), level=self.level + 1)
            return is_split
        elif isinstance(self.b, FishNum):
            is_split |= self.b.split()
        return is_split

    def reset(self):
        self.add_right = 0
        self.add_left = 0
        self.is_explode = False
        self.is_split = False
        if isinstance(self.a, FishNum):
            self.a.reset()
        if isinstance(self.b, FishNum):
            self.b.reset()

    def magnitude(self):
        if isinstance(self.a, FishNum):
            a = self.a.magnitude()
        else:
            a = self.a
        if isinstance(self.b, FishNum):
            b = self.b.magnitude()
        else:
            b = self.b
        return a*3 + b*2

    def add_a_side(self, n):
        if isinstance(self.a, FishNum):
            self.a.add_r_side(n)
        else:
            self.a += n

    def add_b_side(self, n):
        if isinstance(self.b, FishNum):
            self.b.add_l_side(n)
        else:
            self.b += n

    def add_r_side(self, n):
        if isinstance(self.b, FishNum):
            self.b.add_r_side(n)
        else:
            self.b += n

    def add_l_side(self, n):
        if isinstance(self.a, FishNum):
            self.a.add_l_side(n)
        else:
            self.a += n

    def __init__(self, a, b, level=0):
        self.level = level
        self.add_left = 0
        self.add_right = 0
        self.is_explode = False
        self.is_split = False
        # left
        if isinstance(a, int):
            self.a = a
        elif isinstance(a, FishNum):
            self.a = FishNum(a.a, a.b, level=level+1)
        else:
            self.a = FishNum(a[0], a[1], level=level+1)
        # right
        if isinstance(b, int):
            self.b = b
        elif isinstance(b, FishNum):
            self.b = FishNum(b.a, b.b, level=level + 1)
        else:
            self.b = FishNum(b[0], b[1], level=level+1)


def test():
    a = json.loads('[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]')
    b = json.loads('[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]')
    ideal = '[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]'
    a = FishNum.from_list(a)
    b = FishNum.from_list(b)
    r = FishNum(a, b)
    print(f'after addition: {r}')
    action = True
    while action:
        # begin_state = f'{r}'
        a_explode = r.explode()
        if a_explode:
            print(f'after explode: {r}')
            continue
        a_split = r.split()
        if a_split:
            print(f'after split: {r}')
        action = a_split | a_explode
        r.reset()
    print(f'result: {r}')
    print(f'ideal : {ideal}')
    print(f'magnitude: {r.magnitude()}')
    return 0


def solve():
    data = get_input()
    # read
    addings = []
    for item in data:
        fish_num = json.loads(item.replace('\n', ''))
        addings.append(fish_num)
    # sum
    result = None
    i = 0
    for item in addings:
        print(f'level - {i}')
        i += 1
        if result is None:
            result = FishNum.from_list(item)
            print(f'after init: {result}')
        else:
            result = FishNum(result, FishNum.from_list(item))
        # reduced
        action = True
        while action:
            # explode
            a_explode = result.explode()
            if a_explode:
                print(f'after explode: {result}')
                continue
            result.reset()
            # split
            a_split = result.split()
            if a_split:
                print(f'after split: {result}')
            action = a_split | a_explode
            result.reset()
        print('--------------------')
    print(f'{result}')
    final_sum = result.magnitude()
    print(f'{final_sum=}')
    return final_sum

# You guessed 3658 - your answer is too low
# 3639
# 3734

def view_result():
    print(solve())
    # print(test())


if __name__ == '__main__':
    view_result()
