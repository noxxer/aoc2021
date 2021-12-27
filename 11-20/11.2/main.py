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


class Octopus:
    level: int
    flashed: bool

    def __init__(self, level):
        self.flashed = False
        self.level = int(level)

    def add_level(self):
        if not self.flashed:
            self.level += 1

    def flash(self):
        if self.flashed:
            return False
        else:
            self.flashed = True
            self.level = 0


def solve():
    data = get_input()
    octopus_map = []
    flashes_map = []
    total_flashes = 0
    row = 0

    def chain_reaction(row, col):
        chain_flash = 0
        o: Octopus = octopus_map[row][col]
        if o.level > 9 and not o.flashed:
            chain_flash += 1
            o.flash()
            if row > 0:
                # left
                ch_o: Octopus = octopus_map[row - 1][col]
                ch_o.add_level()
                if ch_o.level > 9:
                    chain_flash += chain_reaction(row - 1, col)
                if col > 0:
                    # up-left
                    ch_o: Octopus = octopus_map[row - 1][col - 1]
                    ch_o.add_level()
                    if ch_o.level > 9:
                        chain_flash += chain_reaction(row - 1, col - 1)
                if col < l1 - 1:
                    # down-left
                    ch_o: Octopus = octopus_map[row - 1][col + 1]
                    ch_o.add_level()
                    if ch_o.level > 9:
                        chain_flash += chain_reaction(row - 1, col + 1)
            if row < l1 - 1:
                # right
                ch_o: Octopus = octopus_map[row + 1][col]
                ch_o.add_level()
                if ch_o.level > 9:
                    chain_flash += chain_reaction(row + 1, col)
                if col > 0:
                    # up-right
                    ch_o: Octopus = octopus_map[row + 1][col - 1]
                    ch_o.add_level()
                    if ch_o.level > 9:
                        chain_flash += chain_reaction(row + 1, col - 1)
                if col < l1 - 1:
                    # down-right
                    ch_o: Octopus = octopus_map[row + 1][col + 1]
                    ch_o.add_level()
                    if ch_o.level > 9:
                        chain_flash += chain_reaction(row + 1, col + 1)
            if col > 0:
                # up
                ch_o: Octopus = octopus_map[row][col - 1]
                ch_o.add_level()
                if ch_o.level > 9:
                    chain_flash += chain_reaction(row, col - 1)
            if col < l1 - 1:
                # down
                ch_o: Octopus = octopus_map[row][col + 1]
                ch_o.add_level()
                if ch_o.level > 9:
                    chain_flash += chain_reaction(row, col + 1)
        return chain_flash

    for line in data:
        octopus_map.insert(row, [])
        flashes_map.insert(row, [])
        col = 0
        for point in line.replace('\n', ''):
            octopus_map[row].insert(col, Octopus(point))
            flashes_map[row].insert(col, False)
            col += 1
        row += 1
    l1 = len(octopus_map)
    print('Init')
    for x in range(l1):
        for y in range(l1):
            o: Octopus = octopus_map[x][y]
            print(end=f'{o.level}')
        print('')
    for step in range(1000):
        total_flashes = 0
        print(f'Step - {step}')
        # add one
        for x in range(l1):
            for y in range(l1):
                o: Octopus = octopus_map[x][y]
                o.level += 1
                o.flashed = False
        # flash
        for x in range(l1):
            for y in range(l1):
                total_flashes += chain_reaction(x, y)
        # show
        for x in range(l1):
            for y in range(l1):
                o: Octopus = octopus_map[x][y]
                if o.flashed:
                    print(end=Fore.LIGHTWHITE_EX + f'{o.level}' + Style.RESET_ALL)
                else:
                    print(end=f'{o.level}')
            print('')
        if total_flashes > l1 * l1 - 1:
            break

    print(f'Total - {total_flashes}')
    return total_flashes


# You guessed 1756


def view_result():
    print(solve())


if __name__ == '__main__':
    view_result()
