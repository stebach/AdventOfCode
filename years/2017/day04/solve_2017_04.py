"""
Solution for day 04 of year 2017
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    return tuple(line.strip().split(" "))

def check_no_dubles(data, check_anagrams = False):
    if check_anagrams:
        data = tuple(["".join(sorted([*x])) for x in data])
    for x in data:
        if data.count(x) > 1:
            return False
    return True

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = sum([check_no_dubles(x) for x in data])

    # Part 2
    solution2 = sum([check_no_dubles(x, True) for x in data])

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

