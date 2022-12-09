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

def scenic_tree_score(fname: str = 'input.txt'):
    with open(fname, 'r') as f:
        lines = f.readlines()
    
    grid = [[int(c) for c in l if c != '\n'] for l in lines]
    num_rows = len(grid)
    num_cols = len(grid[0])

    def check_direction(row, col, range, x=True):
        num_trees = 0
        height = grid[row][col]
        
        for i in range:
            num_trees += 1
            if (x and grid[i][col] >= height) or (not x and grid[row][i] >= height):
                break
        
        return num_trees

    max_score = -1
    max_position = None
    max_visibilities = None
    for row in range(num_rows):
        for col in range(num_cols):
            # Check each direction
            left = check_direction(row, col, range(row-1, -1, -1), True)
            right = check_direction(row, col, range(row+1, num_rows), True)
            up = check_direction(row, col, range(col-1, -1, -1), False)
            down = check_direction(row, col, range(col+1, num_cols), False)

            score = left*right*up*down

            if score > max_score:
                max_score = score
                max_position = (row, col)
                max_visibilities = {'l': left, 'r': right, 'u': up, 'd': down}

    print(f'Max scenic score is: {max_score} (at position {max_position} with visibilities {max_visibilities}')                

if __name__ == '__main__':
    if len(sys.argv) == 2:
        count_visible_trees(sys.argv[1])
        scenic_tree_score(sys.argv[1])
    else:
        count_visible_trees()
        scenic_tree_score()