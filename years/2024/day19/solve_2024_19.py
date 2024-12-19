"""
Solution for day 19 of year 2024
"""

import os
from copy import deepcopy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    return {
        'towels':tuple(lines[0].strip().split(', ')),
        'designs':tuple([x.strip() for x in lines[2:]])
    }

def possible_designs(data):
    return [is_possible(design, data['towels']) for design in data['designs']]

def is_possible(design, towels, counts = {}, towels_used = ''):
    design_left = design[len(towels_used):]
    if design_left in counts:
        return counts[design_left]

    count = 0
    for towel in towels:
        towel_string = towels_used + towel
        if towel_string == design:
            count += 1
            continue
        if design.startswith(towel_string):
            count += is_possible(design, towels, counts, towel_string)

    counts[design_left] = count
    return count

def solve(data):
    """Solve the puzzle for the given input"""

    possible = [x for x in possible_designs(data) if x > 0]

    # Part 1
    solution1 = len(possible)

    # Part 2
    solution2 = sum(possible)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

