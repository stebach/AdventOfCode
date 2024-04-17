"""
Solution for day 09 of year 2022
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    line = line.strip().split(' ')    
    return tuple([line[0], int(line[1])])

def count_tail_pos(data, line_length=2):
    visited = set([(0,0)])
    knots = []
    while len(knots) < line_length:
        knots.append((0,0))
    directions = {
        'R': (1,0),
        'L': (-1,0),
        'U': (0,-1),
        'D': (0,1),
    }
    for instruction in data:
        for step in range(instruction[1]):
            knots[0] = (knots[0][0] + directions[instruction[0]][0], knots[0][1] + directions[instruction[0]][1])
            move_tail(knots)
            visited.add(knots[-1])

    return len(visited)

def move_tail(knots):
    for idx in range(1, len(knots)):
        x_diff = knots[idx-1][0] - knots[idx][0]
        y_diff = knots[idx-1][1] - knots[idx][1]
        debug = False
        if abs(x_diff) > 1:
            if y_diff == 0:
                knots[idx] = (knots[idx][0] + int(x_diff/2), knots[idx][1])
            else:
                knots[idx] = (knots[idx][0] + int(x_diff/2), knots[idx][1] + int(y_diff/abs(y_diff)))
        elif abs(y_diff) > 1:
            if x_diff == 0:
                knots[idx] = (knots[idx][0], knots[idx][1] + int(y_diff/2))
            else:
                knots[idx] = (knots[idx][0] + int(x_diff/abs(x_diff)), knots[idx][1] + int(y_diff/2))

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = count_tail_pos(data)

    # Part 2
    solution2 = count_tail_pos(data, 10)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

