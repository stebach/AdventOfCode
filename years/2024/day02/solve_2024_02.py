"""
Solution for day 02 of year 2024
"""

import os
from copy import deepcopy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        # as tuple (strings) with parse_line
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    line = tuple([int(x) for x in line.strip().split()])
    return line

def is_safe(data, tolerate_bad_level = False, skip = -1):
    direction = 1
    localdata = list(deepcopy(data))
    if tolerate_bad_level:
        if len(localdata) > skip:
            del localdata[skip]
        else:
            return False
    if localdata[1] < localdata[0]:
        direction = -1
    for i in range(0, len(localdata) - 1):
        diff = (localdata[i + 1] - localdata[i]) / direction
        if diff < 1 or diff > 3:
            if tolerate_bad_level:
                return is_safe(data, True, skip + 1)
            return False
    return True

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = [is_safe(x) for x in data].count(True)
    # Part 2
    solution2 = [is_safe(x, True) for x in data].count(True)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
