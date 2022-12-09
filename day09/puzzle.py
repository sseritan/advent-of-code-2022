"""Day 9
example.txt 2 -> Part 1 example, should visit 13
input.txt 2 -> Part 1 solution
example.txt [10] -> Part 2 example, should visit 1
example2.txt [10] -> Part 2 example 2, should visit 36
[input.txt] [10] -> Part 2 solution
"""

import sys

def count_tail_locations(fname: str = 'input.txt', num_knots: int = 10):
    with open(fname, 'r') as f:
        lines = f.readlines()

    knot_locations = [[0, 0] for _ in range(num_knots)]
    
    visited_T_locations = set()
    visited_T_locations.add(tuple(knot_locations[-1]))
    def update(dir):
        # Update head
        if dir == 'R':
            knot_locations[0][0] += 1
        elif dir == 'L':
            knot_locations[0][0] += -1
        elif dir == 'U':
            knot_locations[0][1] += 1
        elif dir == 'D':
            knot_locations[0][1] += -1
        else:
            raise ValueError(f'Invalid direction {dir}')
    
        # Update trailing knots
        for i in range(num_knots-1):
            dx = knot_locations[i][0] - knot_locations[i+1][0]
            dy = knot_locations[i][1] - knot_locations[i+1][1]

            if abs(dx) > 1 or abs(dy) > 1:
                xscale = 1 if dx > 0 else -1
                knot_locations[i+1][0] += xscale * min(1, abs(dx))

                yscale = 1 if dy > 0 else -1
                knot_locations[i+1][1] += yscale * min(1, abs(dy))
            
        visited_T_locations.add(tuple(knot_locations[-1]))

    for l in lines:
        dir, num_moves = l.split()
        for _ in range(int(num_moves)):
            update(dir)

    print(f'Number of locations visited by tail: {len(visited_T_locations)}')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        count_tail_locations(sys.argv[1])
    elif len(sys.argv) == 3:
        count_tail_locations(sys.argv[1], int(sys.argv[2]))
    else:
        count_tail_locations()