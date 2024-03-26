"""
Solution for day 01 of year 2021
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(lambda line: int(line.strip()), inputdata.readlines()))

def get_increases(data, window = 1):
    localdata = [sum(data[x[0]:x[0]+window]) for x in enumerate(data) if x[0] < len(data) + 1 - window]
    return sum([1 if x[1] > localdata[x[0]-1] else 0 for x in enumerate(localdata) if x[0] > 0])


def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = get_increases(data)

    # Part 2
    solution2 = get_increases(data, 3)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
