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

def score_inverse_strategy(fname: str = 'input.txt') -> int:
    with open(fname, 'r') as f:
        lines = f.readlines()
    
    outcome_score = {
        'X': 0, # Lose
        'Y': 3, # Draw
        'Z': 6, # Win
    }

    shape_score = {
        'A X': 3, 'B Z': 3, 'C Y': 3, # Scissors
        'A Y': 1, 'B X': 1, 'C Z': 1, # Rock
        'A Z': 2, 'B Y': 2, 'C X': 2, # Paper
    }

    score = 0
    for l in lines:
        score += shape_score[l[:3]] + outcome_score[l[2]]
    
    print(f'Inverse strategy score is {score}')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        score_strategy(sys.argv[1])
        score_inverse_strategy(sys.argv[1])
    else:
        score_strategy()
        score_inverse_strategy()
