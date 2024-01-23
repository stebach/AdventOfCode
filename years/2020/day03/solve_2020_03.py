"""
Solution for day 03 of year 2020
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(lambda line: line.strip(), inputdata.readlines()))

def count_trees(data, right, down):
    x = 0
    y = 0
    count = 0
    while y < len(data):
        if data[y][x%len(data[0])] == '#':
            count += 1
        y += down
        x += right
    return count

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = count_trees(data, 3, 1)

    # Part 2
    solution2 = solution1 * count_trees(puzzle_input, 1, 1) * count_trees(puzzle_input, 5, 1) * count_trees(puzzle_input, 7, 1) * count_trees(puzzle_input, 1, 2)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
