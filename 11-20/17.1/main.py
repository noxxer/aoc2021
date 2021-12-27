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
    data = 'target area: x=236..262, y=-78..-58'
    # x_min = 20
    # x_max = 30
    # y_min = -5
    # y_max = -10
    x_min = 236
    x_max = 262
    y_min = -58
    y_max = -78
    y_result = 0
    max_speed = 100
    for xs in range(max_speed):
        for ys in range(-1 * max_speed, max_speed):
            print(f'{xs=} {ys=}')
            x_speed = xs
            y_speed = ys
            x = 0
            y = 0
            y_flight_max = 0
            flight = True
            catch = False
            path = []
            while flight:
                # step
                x += x_speed
                y += y_speed
                path.append((x, y))
                if y_flight_max < y:
                    y_flight_max = y
                if x_speed > 0:
                    x_speed -= 1
                elif x_speed < 0:
                    x_speed += 1
                y_speed -= 1
                # test area
                if x_min <= x <= x_max and y_min >= y >= y_max:
                    if y_result < y_flight_max:
                        y_result = y_flight_max
                    flight = False
                if x < 0 or x > x_max + 20 or y < y_max:
                    flight = False
            if y_flight_max > 0 and path:
                print(f'{y_flight_max=}: {path=}')
    return y_result


def view_result():
    print(solve())


if __name__ == '__main__':
    view_result()
