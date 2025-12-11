"""
Solution for day 11 of year 2025
"""

import os
import collections
from functools import lru_cache
    #import matplotlib.pyplot as plt


def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    result = []
    Path = collections.namedtuple('Path', ['source', 'targets'])

    for line in lines:
        source, targets = line.strip().split(": ")
        result.append(Path(source, tuple(targets.split(" "))))
    return tuple(result)


@lru_cache(maxsize=None)
def count_recursive(data, current, end, must_contain, contained=0):
    if current in must_contain:
        contained += 1
    result = current == end and len(must_contain) == contained
    if current != end:
        for path in data:
            if path.source == current:
                for target in path.targets:
                    result += count_recursive(data, target, end, must_contain, contained)
    return result

def count_all_paths(data, start, end, must_contain=()):
    return count_recursive(data, start, end, must_contain)

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = count_all_paths(data, 'you', 'out')

    # Part 2
    solution2 = count_all_paths(data, 'svr', 'out', ('fft','dac'))

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
