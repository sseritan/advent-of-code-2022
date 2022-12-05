"""Day 5
"""

import sys

def rearrange_crates(fname: str = 'input.txt') -> None:
    with open(fname, 'r') as f:
        lines = f.readlines()

    # Run through and read how many stacks
    for l in lines:
        if l.startswith(' 1'):
            num_stacks = int(l.split()[-1])

    crate_layout = True
    stacks = [[] for _ in range(num_stacks)] # Objs are bottom to top
    for l in lines:
        if crate_layout is True:
            # We are reading the layout
            try:
                for i in range(num_stacks):
                    if l[1+4*i] != ' ':
                        stacks[i].insert(0, l[1+4*i])
            except IndexError:
                # Separator line, switch to next logic block
                crate_layout = False
        else:
            entries = l.split()
            num_crates = int(entries[1])
            from_stack = int(entries[3]) - 1
            to_stack = int(entries[5]) - 1
        
            for _ in range(num_crates):
                crate = stacks[from_stack].pop()
                stacks[to_stack].append(crate)
    
    top = "".join([stacks[i][-1] for i in range(num_stacks)])
    print(f'Top crates after rearrangement: {top}')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        rearrange_crates(sys.argv[1])
    else:
        rearrange_crates()