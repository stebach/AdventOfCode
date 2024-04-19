"""
Solution for day 11 of year 2022
"""

import os
from math import gcd, floor
from copy import deepcopy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    result = []
    while len(lines):
        line = lines.pop(0).strip()
        if len(line) == 0:
            continue
        monkey = {
            'test_true': 0,
            'test_false': 1,
            'inspections': 0
        }
        monkey['items'] = [int(x) for x in lines.pop(0).strip()[16:].split(', ')]
        line = lines.pop(0).strip()[21:].split(' ')
        operation_type = 1 if line[0] == '*' else 2
        if line[1] == 'old':
            monkey['operation'] = (operation_type,)
        else:
            monkey['operation'] = (operation_type,int(line[1]))
        monkey['test'] = int(lines.pop(0).strip()[19:])
        monkey['test_true'] = int(lines.pop(0).strip()[25:])
        monkey['test_false'] = int(lines.pop(0).strip()[26:])

        result.append(monkey)

    return tuple(result)

def monkey_business_level(data, rounds, calmdown = True):
    monkeys = deepcopy(data)
    lcmval = lcm([x['test'] for x in monkeys])
    for round in range(rounds):
        for monkey in monkeys:
            while len(monkey['items']) > 0:
                item = monkey['items'].pop(0)
                monkey['inspections'] += 1
                operation_val = item
                if len(monkey['operation']) > 1:
                    operation_val = monkey['operation'][1]
                if monkey['operation'][0] == 1:
                    item *= operation_val
                else:
                    item += operation_val
                if calmdown:
                    item = floor(item/3)
                
                if item % lcmval == 0:
                    item = lcmval
                else:
                    item = item % lcmval
                if item % monkey['test'] == 0:
                    monkeys[monkey['test_true']]['items'].append(item)
                else:
                    monkeys[monkey['test_false']]['items'].append(item)
    sorted_monkeys = sorted(monkeys, key=lambda x: x['inspections'], reverse=True)
    return sorted_monkeys[0]['inspections'] * sorted_monkeys[1]['inspections']

def lcm(numbers):
    while len(numbers) > 1:
        a = numbers.pop(0)
        b = numbers.pop(0)
        numbers.append(abs(a*b) // gcd(a, b))
    return numbers[0]

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = monkey_business_level(data, 20)

    # Part 2
    solution2 = monkey_business_level(data, 10_000, False)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
