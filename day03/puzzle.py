"""Day 3
"""

import sys

def compartment_priorities(fname: str = 'input.txt') -> int:
    with open(fname, 'r') as f:
        lines = f.readlines()

    intersections = ''
    for l in lines:
        comp_size = len(l) // 2
        comp1 = set(l[:comp_size])
        comp2 = set(l[comp_size:])

        intersections += comp1.intersection(comp2).pop()

    priorities = {c: i+1 for i,c in enumerate('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')}

    priority = sum([priorities[i] for i in intersections])
    
    print(f'Sum of compartment overlap priorities is {priority}')

def group_badge_priorities(fname: str = 'input.txt') -> int:
    with open(fname, 'r') as f:
        lines = f.readlines()

    intersections = ''
    num_groups = len(lines) // 3
    for i in range(num_groups):
        elf1 = set(lines[3*i + 0][:-1])
        elf2 = set(lines[3*i + 1][:-1])
        elf3 = set(lines[3*i + 2][:-1])

        intersections += elf1.intersection(elf2).intersection(elf3).pop()

    priorities = {c: i+1 for i,c in enumerate('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')}

    priority = sum([priorities[i] for i in intersections])
    
    print(f'Sum of group badge priorities is {priority}')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        compartment_priorities(sys.argv[1])
        group_badge_priorities(sys.argv[1])
    else:
        compartment_priorities()
        group_badge_priorities()