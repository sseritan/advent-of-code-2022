"""Day 11
For easy parsing, assume input has one empty line at the start
"""

import numpy as np
import sys

MONKEYS = []

class Monkey(object):
    def __init__(self, lines):
        # Starting items
        items = lines[0].split(': ')[1]
        self.items = [int(item) for item in items.split(', ')]

        # Operation
        self.op = lines[1].split()[-2]
        assert self.op in '*+', "Invalid op"
        self.op_value = 'old' if lines[1].endswith('old\n') else int(lines[1].split()[-1])

        # Test
        self.div_value = int(lines[2].split()[-1])

        # True/false
        self.true_monkey = int(lines[3].split()[-1])
        self.false_monkey = int(lines[4].split()[-1])
    
        self.num_inspects = 0

    def take_turn(self):
        for item in self.items:
            # Inspect/update worry
            op_val = item if self.op_value == 'old' else self.op_value
            if self.op == '*':
                item *= op_val
            else:
                item += op_val
            
            # Integer divide by 3 for surviving inspection
            item //= 3

            # Test and give item
            if item%self.div_value == 0:
                MONKEYS[self.true_monkey].items.append(item)
            else:
                MONKEYS[self.false_monkey].items.append(item)

            self.num_inspects += 1
        
        # Empty queue
        self.items = []

def compute_monkey_business(fname: str = 'input.txt', num_rounds: int = 20, num_active: int = 2):
    with open(fname, 'r') as f:
        lines = f.readlines()

    num_monkeys = len(lines) // 7
    for i in range(num_monkeys):
        MONKEYS.append(Monkey(lines[7*i+2:7*(i+1)]))

    # Do all monkey business
    for i in range(num_rounds):
        for monkey in MONKEYS:
            monkey.take_turn()
    
    # Sort and get top monkeys
    activity = sorted([m.num_inspects for m in MONKEYS], reverse=True)
    
    monkey_business = 1
    for i in range(num_active):
        monkey_business *= activity[i]

    print(f'Monkey business for top {num_active} monkeys after {num_rounds} rounds: {monkey_business}')
    
    

if __name__ == '__main__':
    if len(sys.argv) == 2:
        compute_monkey_business(sys.argv[1])
    else:
        compute_monkey_business()