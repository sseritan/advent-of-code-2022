"""Day 4
"""

import sys

def find_nested_interval(fname: str = 'input.txt') -> None:
    with open(fname, 'r') as f:
        lines = f.readlines()

    num_nested = 0
    num_overlaps = 0
    for i, l in enumerate(lines):
        interval1, interval2 = l[:-1].split(',') if r'\n' in l else l.split(',')
        start1, end1 = interval1.split('-')
        start2, end2 = interval2.split('-')
        start1 = int(start1)
        end1 = int(end1)
        start2 = int(start2)
        end2 = int(end2)

        if (start1 >= start2 and end1 <= end2) \
            or (start2 >= start1 and end2 <= end1):
            num_nested += 1
        
        if (start1 >= start2 and start1 <= end2) \
            or (start2 >= start1 and start2 <= end1):
            num_overlaps += 1
    
    print(f'Number of nested intervals is {num_nested}')
    print(f'Number of overlapping intervals is {num_overlaps}')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        find_nested_interval(sys.argv[1])
    else:
        find_nested_interval()