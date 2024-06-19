"""
Solution for day 06 of year 2017
"""

import os
from copy import deepcopy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return list(map(parse_line, inputdata.readlines()))[0]

def parse_line(line):
    return [int(x) for x in line.strip().split("\t")]

def loop_size(data, actual_size = False):
    local = deepcopy(data)

    seen = set([])
    count = 0
    keys = {}

    while tuple(local) not in seen:
        count += 1
        seen.add(tuple(local))
        keys[tuple(local)] = count
        val = max(local)
        idx = local.index(val)
        local[idx] = 0

        while val > 0:
            idx += 1
            local[idx % len(local)] += 1
            val -= 1

    if actual_size:
        return count - keys[tuple(local)] + 1
    return count

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = loop_size(data)

    # Part 2
    solution2 = loop_size(data, True)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
