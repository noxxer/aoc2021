import pathlib
import pprint
from colorama import init, Fore, Back, Style

init()


def get_input():
    script_dir = pathlib.Path(__file__).parent.absolute()
    lines = []
    with open(f'{script_dir}/input.txt') as file:
        for line in file:
            lines.append(line)
    return lines


def int2(lst: list) -> int:
    return int(''.join(lst), 2)


def read_part(bits: list) -> dict:
    version = int2(bits[:3])
    p_type = int2(bits[3:6])
    bits[:] = bits[6:]
    value = []
    sub_packs = []
    if p_type == 4:
        while True:
            first_byte = bits[0]
            value += bits[1:5]
            bits[:] = bits[5:]
            if first_byte == '0':
                break
        value = int2(value)
    else:
        # I
        length_type = bits[0]
        if length_type == '0':
            # 15
            length = int2(bits[1:16])
            sub_message = bits[16: 16 + length]
            bits[:] = bits[16 + length:]
            while sub_message and len(sub_message) > 6:
                sub_pack = read_part(sub_message)
                sub_packs.append(sub_pack)
        else:
            # 11
            length = int2(bits[1:12])
            bits[:] = bits[12:]
            for i in range(length):
                sub_pack = read_part(bits)
                sub_packs.append(sub_pack)
    return {
        'version': version,
        'type': p_type,
        'value': value,
        'sub_packs': sub_packs,
    }


def sum_version(d: dict):
    sv = 0
    if 'version' in d:
        sv += d['version']
    if 'sub_packs' in d:
        for sp in d['sub_packs']:
            sv += sum_version(sp)
    return sv

def solve():
    data = get_input()
    data_value = data[0].replace('\n', '')
    bin_packet = []
    for ch in data_value:
        bin_packet.extend(bin(int(ch, 16))[2:].zfill(4))
    r = read_part(bin_packet)
    sum_ver = sum_version(r)

    pprint.pprint(r, indent=4)
    return sum_ver


def view_result():
    print(solve())


if __name__ == '__main__':
    view_result()
