"""
Solution for day 18 of year 2023
"""

import os
import regex
from math import ceil

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    match = regex.findall(r'^([RLUD]) ([0-9]+) \((#[0-9a-f]+)\)$', line.strip())
    directions = {
        'U': (0,-1),
        'D': (0,1),
        'L': (-1,0),
        'R': (1,0),
    }
    return (directions[match[0][0]], int(match[0][1]), match[0][2])

def get_area(data):
    pos = (0,0)
    corners = []

    for dig in data:
        pos = (pos[0] + dig[0][0] * dig[1], pos[1] + dig[0][1] * dig[1])
        corners.append(pos)
    sum1 = 0;
    sum2 = 0;
    for x in range(len(corners)):
        y = (x + 1) % len(corners)
        sum1 += corners[x][0] * corners[y][1]
        sum2 += corners[x][1] * corners[y][0]
    
    return ceil((1 + sum([x[1] for x in data])) / 2) + int(abs(sum1-sum2)/2)

def part1(data):
    """Solve part 1"""
    return get_area(data)

def translate(data):
    directions = {
        '3': (0,-1),
        '1': (0,1),
        '2': (-1,0),
        '0': (1,0),
    }
    return (directions[data[2][6]], int(data[2][1:6], 16))

def part2(data):
    """Solve part 2"""
    return get_area(tuple(map(translate, data)))

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
