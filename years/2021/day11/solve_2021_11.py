"""
Solution for day 11 of year 2021
"""

import os
from copy import copy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return list(map(parse_line, inputdata.readlines()))

def parse_line(line):
    return [int(x) for x in [*line.strip()]]

def step(data):
    flashcount = 0
    local_map = [[y+1 for y in x] for x in data]
    while sum([sum([1 for y in x if y == 10]) for x in local_map]) > 0:
        local_map = [[y if y < 10 or y == 30 else 20 for y in x] for x in local_map]
        for y in range(10):
            for x in range(10):
                if local_map[y][x] == 20:
                    flashcount += 1
                    check_x_from = x
                    check_x_to = x
                    check_y_from = y
                    check_y_to = y
                    if x > 0:
                        check_x_from = x - 1
                    if x < 9:
                        check_x_to = x + 1
                    if y > 0:
                        check_y_from = y - 1
                    if y < 9:
                        check_y_to = y + 1

                    for check_y in range(check_y_from, check_y_to + 1):
                        for check_x in range(check_x_from, check_x_to + 1):
                            if local_map[check_y][check_x] < 10:
                                local_map[check_y][check_x] += 1

        local_map = [[y if y < 20 else 30 for y in x] for x in local_map]
    local_map = [[0 if y == 30 else y for y in x] for x in local_map]
    return {
        'map': local_map,
        'flashes': flashcount
    }

def count_flashes(data, steps):
    total = 0
    local_data = { 'map': copy(data) }
    for s in range(steps):
        local_data = step(local_data['map'])
        total += local_data['flashes']
    return total

def steps_for_full_flash(data):
    steps = 0
    local_data = { 'map': copy(data), 'flashes': 0 }
    while local_data['flashes'] < 100:
        steps += 1
        local_data = step(local_data['map'])

    return steps

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = count_flashes(data, 100)

    # Part 2
    solution2 = steps_for_full_flash(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

