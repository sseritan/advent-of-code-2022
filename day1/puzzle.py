"""Day 1
"""

import sys

# Defaults for Puzzle 2
def find_max_cals(fname: str = 'puzzle1_input.txt', num_elves: int = 3) -> int:
    print(f'Finding max calories from file {fname} with top {num_elves} elves')
    
    with open(fname, 'r') as f:
        lines = f.readlines()
    
    curr_sum = 0
    sums = []
    for l in lines:
        if l == '\n':
            # Empty line, store sum
            sums.append(curr_sum)
            curr_sum = 0
        else:
            # Add to our count for this elf
            curr_sum += int(l)
    
    # Make sure last sum is accounted for too
    if curr_sum != 0:
        sums.append(curr_sum)
    
    # Sort
    sorted_sums = sorted([(s, i) for i, s in enumerate(sums)], reverse=True)

    total_calories = sum([x[0] for x in sorted_sums[:num_elves]])
    elves = [x[1]+1 for x in sorted_sums[:num_elves]]

    print(f'Elves {elves} have the most calories: {total_calories}')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        find_max_cals(sys.argv[1], 1)
    elif len(sys.argv) == 3:
        find_max_cals(sys.argv[1], sys.argv[2])
    else:
        find_max_cals()
