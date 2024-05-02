"""
Solution for day 03 of year 2015
"""

import os
from copy import deepcopy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    line = line.strip()
    directions = {
        '<': (-1, 0),
        '>': (1, 0),
        '^': (0, -1),
        'v': (0, 1),
    }
    return [directions[x] for x in line]

def number_of_houses(data, with_robo_santa = False):
    pos = (0,0)
    pos2 = (0,0)
    houses = set([pos])

    moves = deepcopy(data)

    while len(moves) > 0:
        move = moves.pop(0)
        pos = (pos[0] + move[0], pos[1] + move[1])
        houses.add(pos)
        if with_robo_santa and len(moves) > 0:
            move = moves.pop(0)
            pos2 = (pos2[0] + move[0], pos2[1] + move[1])
            houses.add(pos2)

    return len(houses)


def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = number_of_houses(data[0])

    # Part 2
    solution2 = number_of_houses(data[0], True)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

