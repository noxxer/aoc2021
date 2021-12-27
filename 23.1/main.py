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


class Maze:
    def __init__(self, maze: list, cost: int = 0):
        self.maze = maze
        self.cost = cost

    def get_smart_mazes(self) -> list:
        if self.done():
            return []
        for key, value in self.pos.items():
            if key == 'A' and value[0] != 3:
                return []
            if key == 'B' and value[0] != 5:
                return []
            if key == 'C' and value[0] != 7:
                return []
            if key == 'D' and value[0] != 9:
                return []
        return []

    def done(self) -> bool:
        for key, value in self.pos.items():
            if key == 'A' and value[0] != 3:
                return False
            if key == 'B' and value[0] != 5:
                return False
            if key == 'C' and value[0] != 7:
                return False
            if key == 'D' and value[0] != 9:
                return False
        return True


def solve():
    # https://adventofcode.com/2021/day/21
    data = get_input()
    a_stack = []
    b_stack = []
    c_stack = []
    d_stack = []
    for y in range(5):
        line = data[y].replace('\n', '')
        for x in range(len(line)):
            ch = line[x]
            if ch not in ['A', 'B', 'C', 'D']:
                continue
            if x == 3:
                a_stack.append(ch)
            elif x == 5:
                b_stack.append(ch)
            elif x == 7:
                c_stack.append(ch)
            elif x == 9:
                d_stack.append(ch)
    pos = {
        'A': [],
        'B': [],
        'C': [],
        'D': [],
    }
    for i in range(2):
        ch = str(a_stack.pop())
        pos[ch].append((2, 1 + i))
        ch = str(b_stack.pop())
        pos[ch].append((4, 1 + i))
        ch = str(c_stack.pop())
        pos[ch].append((6, 1 + i))
        ch = str(d_stack.pop())
        pos[ch].append((8, 1 + i))
    m = Maze(pos=pos, cost=0)
    mset = [m, ]
    best_maze = None
    best_cost = 1000000
    while len(mset) > 0:
        m = mset.pop()
        mset.extend(m.get_smart_mazes())
        if m.done() and m.cost < best_cost:
            best_maze = m
            best_cost = m.cost
            print(f'{best_maze=}')
    print(f'Total - {best_cost=}')
    return best_cost


# You guessed 16393
# You guessed 16565
# You guessed 16161 - your answer is too high
# 16159 is too high
# 16177


def view_result():
    print(solve())


if __name__ == '__main__':
    view_result()
