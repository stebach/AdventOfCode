"""
Solution for day 08 of year 2023
"""

import os
from functools import reduce
from math import gcd

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(lambda line: line.strip(), inputdata.readlines()))

def parse_lines(lines):
    return tuple([
        [int(x) for x in [*lines[0].translate(str.maketrans('LR','01'))]],
        {x[0:3] : [x[7:10], x[12:15]] for x in lines[2:]}
    ])

def part1(data):
    """Solve part 1"""
    steps = 0
    location = 'AAA'
    while location != 'ZZZ':
        location = data[1][location][data[0][steps % len(data[0])]]
        steps = steps + 1

    return steps

def part2(data):
    """Solve part 2"""
    first_z = []
    locations = [x for x in list(data[1].keys()) if x[2] == 'A']
    for location in locations:
        steps = 0
        while location[2] != 'Z':
            location = data[1][location][data[0][steps % len(data[0])]]
            steps = steps + 1
        first_z = first_z + [steps]

    return reduce(lambda x, y: abs(x * y) // gcd(x, y) , first_z)

def solve(data):
    """Solve the puzzle for the given input"""
    data = parse_lines(data)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
