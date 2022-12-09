"""Day 8
"""

import sys

def count_visible_trees(fname: str = 'input.txt'):
    with open(fname, 'r') as f:
        lines = f.readlines()

    grid = [[int(c) for c in l if c != '\n'] for l in lines]
    num_rows = len(grid)
    num_cols = len(grid[0])

    visible_trees = {}
    for row in range(num_rows):
        left = -1 
        for col in range(num_cols):
            if grid[row][col] > left:
                if (row, col) in visible_trees:
                    visible_trees[row, col].append('left')
                else:
                    visible_trees[row, col] = ['left']
                left = grid[row][col]

    for row in range(num_rows):
        right = -1
        for col in range(num_cols-1, -1, -1):    
            if grid[row][col] > right:
                if (row, col) in visible_trees:
                    visible_trees[row, col].append('right')
                else:
                    visible_trees[row, col] = ['right']
                right = grid[row][col]
    
    for col in range(num_cols):
        top = -1
        for row in range(num_rows):
            if grid[row][col] > top:
                if (row, col) in visible_trees:
                    visible_trees[row, col].append('top')
                else:
                    visible_trees[row, col] = ['top']
                top = grid[row][col]
    
    for col in range(num_cols):
        bottom = -1
        for row in range(num_rows-1, -1, -1):
            if grid[row][col] > bottom:
                if (row, col) in visible_trees:
                    visible_trees[row, col].append('bottom')
                else:
                    visible_trees[row, col] = ['bottom']
                bottom = grid[row][col]

    #print(visible_trees)
    print(f'Visible trees: {len(visible_trees)}')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        count_visible_trees(sys.argv[1])
    else:
        count_visible_trees()