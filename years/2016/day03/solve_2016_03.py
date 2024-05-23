"""
Solution for day 03 of year 2016
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    return tuple([int(x) for x in line.strip().split(' ') if x != ''])

def count_valid_triangles(data):
    return sum([y[2] < y[0] + y[1] for y in [sorted(x) for x in data]])

def count_valid_triangles_vertical(data):
    vertical = [[sorted([data[x*3][0],data[x*3+1][0],data[x*3+2][0]]),sorted([data[x*3][1],data[x*3+1][1],data[x*3+2][1]]),sorted([data[x*3][2],data[x*3+1][2],data[x*3+2][2]])] for x in range(len(data) // 3)]
    return sum([y[2] < y[0] + y[1] for y in [x for line in vertical for x in line]])

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = count_valid_triangles(data)

    # Part 2
    solution2 = count_valid_triangles_vertical(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
