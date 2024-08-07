"""
Solution for day 15 of year 2017
"""

import os
from copy import deepcopy
def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    return int(line.strip()[24:])

def get_count(data, pairs=40_000_000, multiples=False):
    local_data = deepcopy(data)
    count = 0
    for x in range(pairs):
        if multiples:
            local_data = [local_data[0] * 16807 % 2147483647, local_data[1] * 48271 % 2147483647]
            while local_data[0] % 4 != 0:
                local_data[0] = local_data[0] * 16807 % 2147483647
            while local_data[1] % 8 != 0:
                local_data[1] = local_data[1] * 48271 % 2147483647
        else:
            local_data = [local_data[0] * 16807 % 2147483647, local_data[1] * 48271 % 2147483647]
        if bin(local_data[0])[2:].zfill(16)[-16:] == bin(local_data[1])[2:].zfill(16)[-16:]:
            count += 1
    return count

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = get_count(data)

    # Part 2
    solution2 = get_count(data, 5_000_000, True)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

