"""
Solution for day 01 of year 2018
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(lambda line: int(line.strip()), inputdata.readlines()))

def part1(data):
    """Solve part 1"""
    return sum(data)

def part2(data):
    """Solve part 2"""
    pos = 0
    found = set([0])
    freq = 0
    while pos == len(found) - 1:
        freq += data[pos % len(data)]
        found |= set([freq])
        pos += 1
    return freq

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
