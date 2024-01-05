"""
Solution for day 14 of year 2019
"""

import os
from math import ceil, floor

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    result = {}
    for line in lines:
        parts = line.strip().split(' => ')
        product = parts[1].split(' ')
        result[product[1]] = (int(product[0]),dict([(y[1], int(y[0])) for y in [x.split(' ') for x in parts[0].split(', ')]]))
    return result

def ore_requirement(recipies, fuel_to_produce):
    available = {}
    needed = {}
    add_to_needed(recipies['FUEL'], fuel_to_produce, needed, available)
    complete = False
    while not complete:
        complete = True
        for x in needed:
            if needed[x] > available[x] and x != 'ORE':
                complete = False
                available[x] += add_to_needed(recipies[x], needed[x] - available[x], needed, available)
                break
    return needed['ORE']

def add_to_needed(recipie, amount, needed, available):
    factor = ceil(amount/recipie[0])
    for part in recipie[1]:
        if part not in needed:
            needed[part] = 0
        if part not in available:
            available[part] = 0
        needed[part] += factor * recipie[1][part]
    return factor * recipie[0]

def fuel_for_ore(recipies, ore):
    check = ore_requirement(recipies, 1)
    step = pow(10,len(str(check)) -2)
    total = 0
    while step >= 1:
        total += step
        check = ore_requirement(recipies, total)
        if check > ore:
            total -= step
            step = floor(step / 10)
    return total

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = ore_requirement(data, 1)

    # Part 2
    solution2 = fuel_for_ore(data, 1_000_000_000_000)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
