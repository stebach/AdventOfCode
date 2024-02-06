"""
Solution for day 15 of year 2020
"""

import os
from queue import deque

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return list(map(lambda line: int(line), inputdata.read().strip().split(',')))

def nth_number(numberlist, n):

    map = dict([[x[1], x[0]] for x in enumerate(numberlist)])
    pos = len(map)
    next = 0
    while pos < n - 1:
        if next in map:
            tmp = pos - map[next]
            map[next] = pos
            next = tmp
        else:
            map[next] = pos
            next = 0
        pos += 1

    return next

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = nth_number(data, 2020)

    # Part 2
    solution2 = nth_number(data, 30000000)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

