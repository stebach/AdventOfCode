"""
Solution for day 05 of year 2021
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    return tuple([tuple([int(y) for y in x.split(',')]) for x in line.strip().split(' -> ')])

def get_overlaps(data, min_overlap, include_diagonal = False):
    overlaps = {}
    for line in data:
        if include_diagonal or line[0][0] == line[1][0] or line[0][1] == line[1][1]:
            key = (line[0][0], line[0][1])
            step = (compare(line[0][0], line[1][0]), compare(line[0][1], line[1][1]))
            stop = (line[1][0] + step[0], line[1][1] + step[1])

            while key != stop:
                if not key in overlaps:
                    overlaps[key] = 0
                overlaps[key] += 1
                key = (key[0] + step[0], key[1] + step[1])

    return len([x for x in overlaps if overlaps[x] >= min_overlap])

def compare(a, b):
    if b > a:
        return 1
    if a > b:
        return -1
    return 0


def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = get_overlaps(data, 2)

    # Part 2
    solution2 = get_overlaps(data, 2, True)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
