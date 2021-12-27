import pathlib
from numpy import loadtxt


def get_input():
    script_dir = pathlib.Path(__file__).parent.absolute()
    lines = []
    with open(f'{script_dir}/input.txt') as file:
        while line := file.readline().rstrip():
            lines.append(line)
    return lines


def get_data_index(data: list) -> dict:
    l = len(data[0])
    data_index = {i: {'0': 0, '1': 0} for i in range(0, l)}
    for item in data:
        for i in range(0, l):
            char = item[i]
            data_index[i][char] += 1
    return data_index


def solve():
    data = get_input()
    l = len(data[0])
    data_index = get_data_index(data)
    for item in data:
        for i in range(0, l):
            char = item[i]
            data_index[i][char] += 1
    oxygen_list = data.copy()
    co2_list = data.copy()
    # oxygen
    for i in range(0, l):
        oxygen_new = []
        oxygen_data_index = get_data_index(oxygen_list)
        if oxygen_data_index[i]['0'] > oxygen_data_index[i]['1']:
            for item in oxygen_list:
                if item[i] == '0':
                    oxygen_new.append(item)
        else:
            for item in oxygen_list:
                if item[i] == '1':
                    oxygen_new.append(item)
        oxygen_list = oxygen_new
        if len(oxygen_list) == 1:
            break
    # co2
    for i in range(0, l):
        co2_new = []
        # co2
        co2_data_index = get_data_index(co2_list)
        if co2_data_index[i]['0'] > co2_data_index[i]['1']:
            for item in co2_list:
                if item[i] == '1':
                    co2_new.append(item)
        else:
            for item in co2_list:
                if item[i] == '0':
                    co2_new.append(item)
        co2_list = co2_new
        if len(co2_list) == 1:
            break
    oxygen_generator_rating = int(oxygen_list[0], 2)
    co2_scrubber_rating = int(co2_list[0], 2)
    life_support_rating = oxygen_generator_rating * co2_scrubber_rating
    return life_support_rating


def view_result():
    print(solve())


if __name__ == '__main__':
    view_result()
