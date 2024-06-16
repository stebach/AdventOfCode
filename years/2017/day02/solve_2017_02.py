"""
Solution for day 02 of year 2017
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    return tuple([int(x) for x in line.strip().split("\t")])

def checksum(data):
    return sum([max(x) - min(x) for x in data])

def checksum2(data):
    return sum([find_divisable(x) for x in data])

def find_divisable(row):
    row = sorted(row, reverse=True)
    for first in range(len(row) - 1):
        for second in range(first + 1, len(row)):
            if row[first] % row[second] == 0:
                return row[first] // row[second]
    return 0

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = checksum(data)

    # Part 2
    solution2 = checksum2(data)
    print(solution2)
    exit()
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
