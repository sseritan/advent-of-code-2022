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
    for i, add_value in enumerate(add_values):
        cycle = i + 1
        # Grab value/signal strength during cycle
        if cycle in target_cycles:
            signal_strengths.append(cycle*X)

        X += add_value

    print(f'Sum of signal strengths: {sum(signal_strengths)}')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        sum_signal_strength(sys.argv[1])
    else:
        sum_signal_strength()