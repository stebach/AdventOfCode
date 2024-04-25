"""
Solution for day 20 of year 2022
"""

import os
from copy import deepcopy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(lambda line: int(line.strip()), inputdata.readlines()))

def decrypt(numbers, key = 1, times = 1):
    orig = tuple([(x[1]*key, x[0]) for x in enumerate(numbers)])
    buffer = list(deepcopy(orig))
    for run in range(times):
        for nr in orig:
            idx = buffer.index(nr)
            del buffer[idx]
            pos = (((idx + nr[0]) % len(buffer)) + len(buffer)) % len(buffer)
            buffer.insert(pos, nr)
    idx = buffer.index([x for x in orig if x[0] == 0][0])
    return buffer[(idx+1000) % len(buffer)][0] + buffer[(idx+2000) % len(buffer)][0] + buffer[(idx+3000) % len(buffer)][0]


def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = decrypt(data)

    # Part 2
    solution2 = decrypt(data, 811589153, 10)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

