"""
Solution for day 01 of year 2023
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        # as one big text
        # return inputdata.read()

        # as tuple (int)
        # return tuple(map(lambda line: int(line.strip()), inputdata.readlines()))

        # as tuple (strings)
        return tuple(map(lambda line: line.strip(), inputdata.readlines()))

def part1(data):
    """Solve part 1"""
    print(data)
    exit()
    return data

def part2(data):
    """Solve part 2"""
    print(data)
    exit()
    return data

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
