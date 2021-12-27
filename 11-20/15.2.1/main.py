import pathlib
from colorama import init, Fore, Back, Style
import networkx as nx

init()


def get_input():
    script_dir = pathlib.Path(__file__).parent.absolute()
    lines = []
    with open(f'{script_dir}/input.txt') as file:
        for line in file:
            lines.append(line)
    return lines


def reduction(value):
    if value > 9:
        return value - 9
    else:
        return value


def solve():
    data = get_input()
    chiton_map = []
    row = 0

    for line in data:
        chiton_map.insert(row, [])
        col = 0
        for point in line.replace('\n', ''):
            chiton_map[row].insert(col, int(point))
            col += 1
        row += 1
    l_y = len(chiton_map)
    l_x = len(chiton_map[0])

    extra_map = []
    for x in range(l_x * 5):
        extra_map.insert(x, [])
        for y in range(l_y * 5):
            extra_map[x].insert(y, 0)

    for x in range(l_x):
        for y in range(l_y):
            value = chiton_map[x][y]
            for x_multi in range(5):
                n_x = x + l_x * x_multi
                for y_multi in range(5):
                    n_y = y + l_y * y_multi
                    n_value = reduction(value + x_multi + y_multi)
                    extra_map[n_x][n_y] = n_value
    l_y = l_y * 5
    l_x = l_x * 5
    print('Init')

    d_graph = nx.DiGraph()
    for x in range(l_x):
        for y in range(l_y):
            if x > 0:  # left
                d_graph.add_weighted_edges_from([((x, y), (x - 1, y), extra_map[x - 1][y]), ])
            if y > 0:  # up
                d_graph.add_weighted_edges_from([((x, y), (x, y - 1), extra_map[x][y - 1]), ])
            if x + 1 < l_x:  # right
                d_graph.add_weighted_edges_from([((x, y), (x + 1, y), extra_map[x + 1][y]), ])
            if y + 1 < l_y:  # down
                d_graph.add_weighted_edges_from([((x, y), (x, y + 1),  extra_map[x][y + 1]), ])
    path = nx.dijkstra_path(d_graph, (0, 0), (l_x - 1, l_y - 1))
    print('--- Best path ---')
    print(path)
    print('--- Best path price ---')
    for x in range(l_x):
        for y in range(l_y):
            if (x, y) in path:
                print(end=Fore.LIGHTWHITE_EX + f'{extra_map[x][y]}' + Style.RESET_ALL)
            else:
                print(end=f'{extra_map[x][y]}')
        print('')
    dijkstra_path_length = nx.dijkstra_path_length(d_graph, (0, 0), (l_x - 1, l_y - 1))
    print(f'Total risk - {dijkstra_path_length}')
    return dijkstra_path_length


# You guessed answer 3012 is too high
# your answer is too low 745
# your answer is too low 2984
# You guessed 3012
# You guessed 3004
# You guessed 3003
# 3002
# low too 2972


def view_result():
    print(solve())


if __name__ == '__main__':
    view_result()
