"""
Solution for day 25 of year 2015
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())


def parse_lines(lines):
    vals = lines[0][:-1].split('at row ')[1].split(', column ')
    return (int(vals[1]), int(vals[0]))

def get_code(data):
    n = data[0] + data[1] - 1
    top = (n * (n + 1)) // 2
    number = top - data[1] + 1

    result = 20151125
    for x in range(1, number):
        result = (result * 252533) % 33554393
    return result

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = get_code(data)

    # Part 2
    solution2 = None

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

