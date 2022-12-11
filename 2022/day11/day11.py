import sys
from dataclasses import dataclass
from typing import List
from functools import reduce
from operator import mul

test = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""

@dataclass
class Monkey():
    id: int
    items: List[int]
    operation: (str, str)
    test: int
    to_if_true: int
    to_if_false: int
    inspections: int

def run(monkeys,relief=lambda w: w//3):
    id_index = {m.id: m for m in monkeys}
    for m in monkeys:
        for item in m.items:
            m.inspections += 1
            if m.operation[1] == 'old':
                op_val = item
            else:
                op_val = int(m.operation[1])
            if m.operation[0] == '+':
                new_worry = (item + op_val)
                new_worry = relief(new_worry)
            elif m.operation[0] == '*':
                new_worry = (item * op_val)
                new_worry = relief(new_worry)
            else:
                raise Error(f'unknown op: {m.operation}')
            if new_worry % m.test == 0:
                new_monkey = id_index[m.to_if_true]
            else:
                new_monkey = id_index[m.to_if_false]
            new_monkey.items.append(new_worry)
        m.items = list()
    return monkeys

def parse_monkey(text):
    lines = text.splitlines()
    # lazy assumptions
    monkey_id = int(lines[0].split()[1][0])
    items = [int(i) for i in lines[1].split(':')[1].split(', ')]
    op = tuple(lines[2].split()[4:])
    test = int(lines[3].split()[-1])
    to_true = int(lines[4].split()[-1])
    to_false = int(lines[5].split()[-1])
    return Monkey(monkey_id, items, op, test, to_true, to_false,0)

def part1(monkeys):
    for i in range(20):
        monkeys = run(monkeys)
    most = sorted(m.inspections for m in monkeys)
    return most[-2] * most[-1]

def product(l):
    return reduce(mul,l,1)

def part2(monkeys):
    relief_factor = product(m.test for m in monkeys)
    for i in range(10000):
        monkeys = run(monkeys,lambda w: w%relief_factor)
    most = sorted(m.inspections for m in monkeys)
    return most[-2] * most[-1]

if __name__ == "__main__":
    if 'test' in sys.argv:
        text = test
    else:
        with open('input') as f:
            text = f.read()

    monkeys = [parse_monkey(block) for block in text.split('\n\n')]
    print(f"Part 1: {part1(monkeys)}")
    # fresh monkeys for part2
    monkeys = [parse_monkey(block) for block in text.split('\n\n')]
    print(f"Part 2: {part2(monkeys)}")
