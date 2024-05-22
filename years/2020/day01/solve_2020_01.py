"""
Solution for day 01 of year 2020
"""

import os
from functools import reduce

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        # as tuple (int)
        return tuple(map(lambda line: int(line.strip()), inputdata.readlines()))

def find_sum(data, target, three=False):
    for x in range(len(data) - (2 if three else 1)):
        for y in range(x, len(data) - (1 if three else 0)):
            if three:
                for z in range(y, len(data)):
                    if data[x] + data[y] + data[z] == target:
                        return (data[x], data[y], data[z])
            else:
                if data[x] + data[y] == target:
                    return (data[x], data[y])

    

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = reduce(lambda a, b: a * b, find_sum(data, 2020))
    # Part 2
    solution2 = reduce(lambda a, b: a * b, find_sum(data, 2020, True))
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

