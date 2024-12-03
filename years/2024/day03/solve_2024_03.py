"""
Solution for day 03 of year 2024
"""

import os
import regex

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return inputdata.read()

def add_up_mul(data, with_conditional_statements = False):
    result = 0
    enabled = True
    for match in regex.finditer(r'mul\((\d+),(\d+)\)|do(n\'t)?\(\)', data):
        if match.group(0) in ('do()', 'don\'t()'):
            enabled = not with_conditional_statements or match.group(0) == 'do()'
        elif enabled:
            result += int(match.group(1)) * int(match.group(2))
    return result

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = add_up_mul(data)
    # Part 2
    solution2 = add_up_mul(data, True)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
