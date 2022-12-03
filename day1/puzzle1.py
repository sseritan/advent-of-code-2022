"""Day 1, Puzzle 1
"""

import sys

def find_max_cals(fname: str = 'puzzle1_input.txt') -> int:
    with open(fname, 'r') as f:
        lines = f.readlines()
    
    curr_sum = 0
    max_sum = 0
    elf = 1
    max_elf = -1
    for l in lines:
        if l == '\n':
            # Empty line, check if this elf has the most calories
            if curr_sum > max_sum:
                max_sum = curr_sum
                max_elf = elf
            elf += 1
            curr_sum = 0
        else:
            # Add to our count for this elf
            curr_sum += int(l)
    
    # Make sure last sum is accounted for too
    if curr_sum > max_sum:
        max_sum = curr_sum

    print(f'Elf {max_elf} has the most calories: {max_sum}')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        find_max_cals(sys.argv[1])
    else:
        find_max_cals()
