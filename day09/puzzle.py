"""Day 9
"""

import sys

def count_tail_locations(fname: str = 'input.txt'):
    with open(fname, 'r') as f:
        lines = f.readlines()

    H = [0, 0]
    T = [0, 0]
    
    visited_T_locations = set()
    visited_T_locations.add(tuple(T))
    def update(dir):
        # Update head
        if dir == 'R':
            H[0] += 1
        elif dir == 'L':
            H[0] += -1
        elif dir == 'U':
            H[1] += 1
        elif dir == 'D':
            H[1] += -1
        else:
            raise ValueError(f'Invalid direction {dir}')
    
        # Update tail
        dx = H[0] - T[0]
        dy = H[1] - T[1]

        if abs(dx) > 1 or abs(dy) > 1:
            xscale = 1 if dx > 0 else -1
            T[0] += xscale * min(1, abs(dx))

            yscale = 1 if dy > 0 else -1
            T[1] += yscale * min(1, abs(dy))
        
        visited_T_locations.add(tuple(T))

    for l in lines:
        dir, num_moves = l.split()
        for _ in range(int(num_moves)):
            update(dir)

    print(f'Number of locations visited by tail: {len(visited_T_locations)}')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        count_tail_locations(sys.argv[1])
    else:
        count_tail_locations()