"""
Solution for day 02 of year 2015
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    return tuple(sorted([int(x) for x in line.strip().split('x')]))

def square_feet_wrapping_paper(data):
    return sum([row[0] * row[1] * 3 + row[0] * row[2] * 2 + row[1] * row[2] * 2 for row in data])

def feet_ribbon(data):
    return sum([row[0]*2 + row[1] * 2 + row[0] * row[1] * row[2] for row in data])

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = square_feet_wrapping_paper(data)

    # Part 2
    solution2 = feet_ribbon(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

