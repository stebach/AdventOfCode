"""
Solution for day 22 of year 2017
"""

import os
from copy import deepcopy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return list(map(parse_line, inputdata.readlines()))

def parse_line(line):
    return list(line.strip())

def count_burst_infections(data, runs = 10_000, states = 2, turn_left = 0, turn_right = 1, inverse_direction = -1):
    local_data = {}
    for row in range(len(data)):
        for col in range(len(data[0])):
            if data[row][col] == '#':
                local_data[str(col) + "__"  + str(row)] = states // 2
    pos = [(len(data[0]) - 1) // 2, (len(data) - 1) // 2]
    direction = [0, -1]
    bursts = 0

    for i in range(runs):
        key = str(pos[0]) + '__' + str(pos[1])
        state = 0
        if key in local_data:
            state = local_data[key]

        if state == turn_left:
            direction = [direction[1], direction[0] * -1]
        elif state == turn_right:
            direction = [direction[1] * -1, direction[0]]
        elif state == inverse_direction:
            direction = [direction[0] * -1, direction[1] * -1]

        local_data[key] = state + 1
        if local_data[key] == states // 2:
            bursts += 1
        elif local_data[key] % states == 0:
            del local_data[key]

        pos[0] += direction[0]
        pos[1] += direction[1]

    return bursts

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = count_burst_infections(data)

    # Part 2
    solution2 = count_burst_infections(data, 10_000_000, 4, 0, 2, 3)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
