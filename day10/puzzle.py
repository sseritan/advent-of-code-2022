"""Day 10
"""

from typing import Iterable
import sys

def sum_signal_strength(fname: str = 'input.txt', target_cycles: Iterable[int] = [20, 60, 100, 140, 180, 220]):
    with open(fname, 'r') as f:
        lines = f.readlines()

    # Read input
    add_values = []
    for l in lines:
        if l.startswith('addx'):
            add_values.extend([0, int(l.split()[-1])])
        elif l.startswith('noop'):
            add_values.append(0)
        else:
            assert "Invalid command"

    X = 1
    signal_strengths = []
    screen_location = 0
    screen_output = ''
    for i, add_value in enumerate(add_values):
        cycle = i + 1
        # Grab value/signal strength during cycle
        if cycle in target_cycles:
            signal_strengths.append(cycle*X)

        if screen_location > X-2 and screen_location < X+2:
            screen_output += '#'
        else:
            screen_output += '.'

        # End of cycle, increment value/move sprite and move screen location
        X += add_value
        if cycle%40 == 0:
            screen_location = 0
            screen_output += '\n'
        else:
            screen_location += 1

    print(f'Sum of signal strengths: {sum(signal_strengths)}')
    print('Screen output:')
    print(screen_output)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        sum_signal_strength(sys.argv[1])
    else:
        sum_signal_strength()