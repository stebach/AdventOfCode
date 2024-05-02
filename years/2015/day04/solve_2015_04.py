"""
Solution for day 04 of year 2015
"""

import os
from hashlib import md5

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(lambda line: line.strip(), inputdata.readlines()))

def find_lowest_key(data, six_zeroes = False):
    for x in range(5_000_000):
        tmp = data + str(x)
        if six_zeroes and md5(tmp.encode()).hexdigest()[0:6] == '000000':
            return x
        elif not six_zeroes and md5(tmp.encode()).hexdigest()[0:5] == '00000':
            return x

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = find_lowest_key(data[0])

    # Part 2
    solution2 = find_lowest_key(data[0], True)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

