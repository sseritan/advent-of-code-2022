"""Day 4
"""

import sys

def find_nested_interval(fname: str = 'input.txt') -> int:
    with open(fname, 'r') as f:
        lines = f.readlines()

    num_nested = 0
    for i, l in enumerate(lines):
        interval1, interval2 = l[:-1].split(',')
        start1, end1 = interval1.split('-')
        start2, end2 = interval2.split('-')

        if (int(start1) >= int(start2) and int(end1) <= int(end2)) \
            or (int(start2) >= int(start1) and int(end2) <= int(end1)):
            num_nested += 1
    
    print(f'Number of nested intervals is {num_nested}')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        find_nested_interval(sys.argv[1])
    else:
        find_nested_interval()