"""
Solution for day 05 of year 2017
"""

import os
from copy import deepcopy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return list(map(parse_line, inputdata.readlines()))

def get_jumps(data, decrease_if_three_or_more = False):
    local = deepcopy(data)
    idx = 0
    count = 0
    while idx < len(local):
        next_idx = idx + local[idx]
        count += 1
        if decrease_if_three_or_more and local[idx] > 2:
            local[idx] -= 1
        else:
            local[idx] += 1
        idx = next_idx
    return count

def parse_line(line):
    line = int(line.strip())
    return line

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = get_jumps(data)

    # Part 2
    solution2 = get_jumps(data, True)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
