"""
Solution for day 01 of year 2015
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    return [-1 if x == ')' else 1 for x in line.strip()]

def get_floor(data):
    return sum(data)

def get_first_pos_for_basement(data):
    pos = 0
    floor = 0
    for x in data:
        floor += x
        pos += 1
        if floor < 0:
            break
    return pos

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = get_floor(data[0])

    # Part 2
    solution2 = get_first_pos_for_basement(data[0])
    
    return solution1, solution2


if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

