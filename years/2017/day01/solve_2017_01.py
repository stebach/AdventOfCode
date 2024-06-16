"""
Solution for day 01 of year 2017
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return inputdata.read().strip()

def captcha(data, halfway = False):
    return sum([int(data[x]) for x in range(len(data)) if data[x] == data[(x + ((len(data) // 2) if halfway else 1)) % len(data)]])

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = captcha(data)

    # Part 2
    solution2 = captcha(data, True)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
