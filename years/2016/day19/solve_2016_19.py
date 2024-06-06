"""
Solution for day 19 of year 2016
"""

import os
from collections import deque

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return int(inputdata.read())

def white_elephant_circle(data, part2 = False):
    if part2:
        queue = deque([x for x in range(data)])
        amount = (len(queue) - 1) // 2
        while len(queue) > 1:
            for x in range(amount):
                queue.append(queue.popleft())
            queue.popleft()
            if amount == 1:
                amount = 0
            else:
                amount = 1
        return queue[0] + 1
    else:
        queue = deque([x for x in range(data)])
        while len(queue) > 1:
            queue.append(queue.popleft())
            queue.popleft()
        return queue.popleft() + 1

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = white_elephant_circle(data)

    # Part 2
    solution2 = white_elephant_circle(data, True)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
