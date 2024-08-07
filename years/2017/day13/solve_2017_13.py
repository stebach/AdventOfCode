"""
Solution for day 13 of year 2017
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    line = [int(x) for x in line.strip().split(": ")]
    return line

def get_severity(data):
    return sum([x[0]*x[1] for x in data if x[0] % ((x[1] - 1) * 2) == 0])

def get_fewest_wait_without_getting_caught(data):
    i = 0
    solution = 0
    while solution == 0:
        solution_found = True
        for y in data:
            if (i + y[0]) % ((y[1] -1) * 2) == 0:
                i = i + 1
                solution_found = False
                break
        if solution_found:
            solution = i
    return solution

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = get_severity(data)

    # Part 2
    solution2 = get_fewest_wait_without_getting_caught(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

