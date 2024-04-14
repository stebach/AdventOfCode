"""
Solution for day 04 of year 2022
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    return tuple([tuple([int(y) for y in x.split('-')]) for x in line.strip().split(',')])

def find_fully_contained(data):
    count = 0
    for line in data:
        if (line[0][0] >= line[1][0] and line[0][1] <= line[1][1]) or (line[0][0] <= line[1][0] and line[0][1] >= line[1][1]):
            count += 1
    return count

def find_overlapping(data):
    count = 0
    for line in data:
        if line[0][1] >= line[1][0] and line[0][0] <= line[1][1]:
            count += 1
    return count

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = find_fully_contained(data)

    # Part 2
    solution2 = find_overlapping(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

