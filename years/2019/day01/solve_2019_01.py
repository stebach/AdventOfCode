"""
Solution for day 01 of year 2019
"""

import os
from math import floor

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(lambda line: int(line.strip()), inputdata.readlines()))

def part1(data):
    """Solve part 1"""
    return sum([floor(x/3) - 2 for x in data])

def part2(data):
    """Solve part 2"""
    total = 0
    for x in data:
        fuel = floor(x/3) - 2
        while fuel >= 6:
            total += fuel
            fuel = floor(fuel/3) - 2
        total += fuel

    return total


def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
