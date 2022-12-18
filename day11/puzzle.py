"""Day 11
For easy parsing, assume input has one empty line at the start
python puzzle.py example.py 20 1 -> Part 1 example, expect 10605
python puzzle.py input.py 20 1 -> Part 1 answer (78678)
python puzzle.py example.py 20 -> Part 2 example,    expect 10197
python puzzle.py example.py 1000 -> Part 2 example,  expect 27019168
python puzzle.py example.py 5000 -> Part 2 example,  expect 677950000
python puzzle.py example.py 10000 -> Part 2 example, expect 2713310158
"""

from typing import Iterable
import sys

MONKEYS = []

class Monkey(object):
    def __init__(self, lines: Iterable[str], index: int) -> None:
        self.index = index

        # Starting items
        self.items = [int(item) for item in lines[0].split(': ')[1].split(', ')]
        self.remainders = None

        # Operation
        self.op = lines[1].split()[-2]
        assert self.op in '*+', "Invalid op"
        self.op_value = 'old' if lines[1].endswith('old\n') else int(lines[1].split()[-1])

        # Test
        self.test_divisor = int(lines[2].split()[-1])

        # True/false
        self.true_monkey = int(lines[3].split()[-1])
        self.false_monkey = int(lines[4].split()[-1])

        self.num_inspects = 0

    def take_part1_turn(self) -> None:
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
            if item%self.test_divisor == 0:
                MONKEYS[self.true_monkey].items.append(item)
            else:
                MONKEYS[self.false_monkey].items.append(item)

            self.num_inspects += 1
        
        # Empty queue
        self.items = []
    
    def take_part2_turn(self) -> None:        
        for item_rems in self.remainders:
            # Inspect/update worry
            new_rems = []
            for i, rem in enumerate(item_rems):
                op_val = rem if self.op_value == 'old' else self.op_value
                if self.op == '*':
                    rem *= op_val
                else:
                    rem += op_val
                new_rems.append(rem%MONKEYS[i].test_divisor)

            # Test and give
            if new_rems[self.index] == 0:
                MONKEYS[self.true_monkey].remainders.append(new_rems)
            else:
                MONKEYS[self.false_monkey].remainders.append(new_rems)
            
            self.num_inspects += 1
        
        # Empty queue
        self.remainders = []

def compute_monkey_business(fname: str = 'input.txt', num_rounds: int = 10000, part: int = 2) -> None:
    num_active = 2 # Hardcoded

    with open(fname, 'r') as f:
        lines = f.readlines()

    num_monkeys = len(lines) // 7
    for i in range(num_monkeys):
        MONKEYS.append(Monkey(lines[7*i+2:7*(i+1)], i))
    
    if part == 2:
        for monkey in MONKEYS:
            monkey.remainders = [[item%m.test_divisor for m in MONKEYS] for item in monkey.items]

    # Do all monkey business
    for i in range(num_rounds):
        for monkey in MONKEYS:
            if part == 1:
                monkey.take_part1_turn()
            else:
                monkey.take_part2_turn()
    
    # Sort and get top monkeys
    activity = sorted([m.num_inspects for m in MONKEYS], reverse=True)
    
    # Compute monkey business
    monkey_business = 1
    for i in range(num_active):
        monkey_business *= activity[i]

    print(f'Monkey business for top {num_active} monkeys after {num_rounds} rounds: {monkey_business}')

if __name__ == '__main__':
    if len(sys.argv) == 3:
        compute_monkey_business(sys.argv[1], num_rounds=int(sys.argv[2]))
    elif len(sys.argv) == 4:
        compute_monkey_business(sys.argv[1], num_rounds=int(sys.argv[2]), part=int(sys.argv[3]))
    else:
        compute_monkey_business()