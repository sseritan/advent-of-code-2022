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
    stacks9000 = [[] for _ in range(num_stacks)] # Objs are bottom to top
    stacks9001 = [[] for _ in range(num_stacks)] # Objs are bottom to top
    for l in lines:
        if crate_layout is True:
            # We are reading the layout
            try:
                for i in range(num_stacks):
                    if l[1+4*i] != ' ':
                        stacks9000[i].insert(0, l[1+4*i])
                        stacks9001[i].insert(0, l[1+4*i])
            except IndexError:
                # Separator line, switch to next logic block
                crate_layout = False
        else:
            entries = l.split()
            num_crates = int(entries[1])
            from_stack = int(entries[3]) - 1
            to_stack = int(entries[5]) - 1
        
            # CrateMover9000 logic
            for _ in range(num_crates):
                crate = stacks9000[from_stack].pop()
                stacks9000[to_stack].append(crate)
            
            # CrateMover9001 logic
            crates = stacks9001[from_stack][-num_crates:]
            stacks9001[to_stack].extend(crates)
            del stacks9001[from_stack][-num_crates:]
    
    top9000 = "".join([stacks9000[i][-1] for i in range(num_stacks)])
    print(f'Top crates after rearrangement with CrateMover9000: {top9000}')

    top9001 = "".join([stacks9001[i][-1] for i in range(num_stacks)])
    print(f'Top crates after rearrangement with CrateMover9001: {top9001}')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        rearrange_crates(sys.argv[1])
    else:
        rearrange_crates()