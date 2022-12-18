"""Day 11
For easy parsing, assume input has one empty line at the start
python puzzle.py example.py 20 3 -> Part 1 example, expect 10605
python puzzle.py input.py 20 3 -> Part 1 answer
python puzzle.py example.py 20 1 -> Part 2 example,    expect 10917
python puzzle.py example.py 1000 1 -> Part 2 example,  expect 27019168
python puzzle.py example.py 5000 1 -> Part 2 example,  expect 677950000
python puzzle.py example.py 10000 1 -> Part 2 example, expect 2713310158
"""

from typing import Iterable
import sys

MONKEYS = []

class Monkey(object):
    def __init__(self, lines: Iterable[str], worry_divisor: int = 1) -> None:
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
    
        self.worry_divisor = worry_divisor
        self.num_inspects = 0

    def take_turn(self) -> None:
        for item in self.items:
            # Inspect/update worry
            op_val = item if self.op_value == 'old' else self.op_value
            if self.op == '*':
                item *= op_val
            else:
                item += op_val
            
            # Integer divide by 3 for surviving inspection
            item //= self.worry_divisor

            # Test and give item
            if item%self.div_value == 0:
                MONKEYS[self.true_monkey].items.append(item)
            else:
                MONKEYS[self.false_monkey].items.append(item)

            self.num_inspects += 1
        
        # Empty queue
        self.items = []

def compute_monkey_business(fname: str = 'input.txt', num_rounds: int = 10000, num_active: int = 2,
    worry_divisor: int = 1) -> None:
    with open(fname, 'r') as f:
        lines = f.readlines()

    num_monkeys = len(lines) // 7
    for i in range(num_monkeys):
        MONKEYS.append(Monkey(lines[7*i+2:7*(i+1)], worry_divisor))

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
    if len(sys.argv) == 4:
        compute_monkey_business(sys.argv[1], num_rounds=int(sys.argv[2]), worry_divisor=int(sys.argv[3]))
    else:
        compute_monkey_business()