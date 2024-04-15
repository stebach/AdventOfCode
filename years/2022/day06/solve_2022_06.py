"""
Solution for day 06 of year 2022
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return inputdata.read().strip()

def find_marker(data, marker_length = 4):
    chars = [*data]
    for x in range(0, len(data) - marker_length + 1):
        if len(set(chars[x:x+marker_length])) == marker_length:
            return x + marker_length

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = find_marker(data)

    # Part 2
    solution2 = find_marker(data, 14)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
