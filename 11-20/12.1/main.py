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


def find_all_paths(graph, start, end, path: list):
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        return [path, ]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if str(node).islower() and str(node) in path:
            continue
        new_paths = find_all_paths(graph, node, end, path)
        for new_path in new_paths:
            if end in new_path:
                if new_path not in paths:
                    paths.append(new_path)
                    print(f'found new: {new_path}')
    return paths


def solve():
    data = get_input()
    graph = {}
    for line in data:
        i, o = line.replace('\n', '').split('-')
        if i in graph:
            graph[i].append(o)
        else:
            graph[i] = [o, ]
        if o in graph:
            graph[o].append(i)
        else:
            graph[o] = [i, ]
    routes = find_all_paths(graph, 'start', 'end', [])
    total_routes = len(routes)
    return total_routes


def view_result():
    print(solve())


if __name__ == '__main__':
    view_result()
