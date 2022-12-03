"""Day 2
"""

import sys

def score_strategy(fname: str = 'input.txt') -> int:
    with open(fname, 'r') as f:
        lines = f.readlines()
    
    shape_score = {
        'X': 1, # Rock
        'Y': 2, # Paper
        'Z': 3, # Scissors
    }

    match_score = {
        'A X': 3, 'B Y': 3, 'C Z': 3, # Draw
        'A Y': 6, 'B Z': 6, 'C X': 6, # Win
        'A Z': 0, 'B X': 0, 'C Y': 0, # Lose
    }

    score = 0
    for l in lines:
        score += match_score[l[:3]] + shape_score[l[2]]
    
    print(f'Strategy score is {score}')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        score_strategy(sys.argv[1])
    else:
        score_strategy()
