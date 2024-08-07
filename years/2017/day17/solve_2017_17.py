"""
Solution for day 17 of year 2017
"""

import os
from collections import deque

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return int(inputdata.read())

def spinlock(steps, values = 2017, after = 2017):
    queue = deque()
    queue.append(0)
    for x in range(values):
        queue.rotate(- (steps + 1))
        queue.appendleft(x+1)
    return queue[(queue.index(after) + 1) % len(queue)]

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = spinlock(data)

    # Part 2
    solution2 = spinlock(data, 50_000_000, 0)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
