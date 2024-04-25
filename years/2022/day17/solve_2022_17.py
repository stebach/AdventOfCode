"""
Solution for day 17 of year 2022
"""

import os
from math import floor

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    return tuple([ord(x) - 61 for x in lines[0].strip()])

def get_height_after_number_of_rocks(data, number_of_rocks):
    shapes = (
        ((2,3), (3,3), (4,3), (5,3)),
        ((3,5), (2,4), (3,4), (4,4), (3,3)),
        ((2,3), (3,3), (4,3), (4,4), (4,5)),
        ((2,3), (2,4), (2,5), (2,6)),
        ((2,3), (3,3), (2,4), (3,4)),
    )
    grid = []
    jet_pattern_index = 0
    rock_shape_index = 0
    rock_shape = [[x[0], x[1] + len(grid)] for x in shapes[rock_shape_index]]

    rock_shape_index += 1

    landings = 0

    check_len = 100
    additional_height = 0
    check_positions = {}

    while True:
        check = [[x[0] + data[jet_pattern_index], x[1]] for x in rock_shape]
        if len([x for x in check if x[0] > 6 or x[0] < 0 or (len(grid) > x[1] and grid[x[1]][x[0]] == 1)]) == 0:
            rock_shape = check
        jet_pattern_index = (jet_pattern_index + 1) % len(data)
        check = [[x[0], x[1] -1] for x in rock_shape]
        if len([x for x in check if x[1] < 0 or (len(grid) > x[1] and grid[x[1]][x[0]] == 1)]) > 0:
            landings += 1
            while len(grid) <= max([x[1] for x in rock_shape]):
                grid.append([0,0,0,0,0,0,0])
            for x in rock_shape:
                grid[x[1]][x[0]] = 1
            
            if len(grid) > check_len:
                last_lines = "".join(["".join([str(y) for y in x]) for x in grid[-check_len:]])
                if last_lines in check_positions and additional_height == 0:
                    loop_rock_count = landings - check_positions[last_lines][0]
                    loop_height_diff = len(grid) - check_positions[last_lines][1]

                    additional_landings = floor((number_of_rocks - landings) / loop_rock_count)
                    additional_height = loop_height_diff * additional_landings
                    landings += additional_landings * loop_rock_count
                check_positions[last_lines] = (landings, len(grid))
            
            if landings == number_of_rocks:
                break

            rock_shape = [[x[0], x[1] + len(grid)] for x in shapes[rock_shape_index]]
            rock_shape_index = (rock_shape_index + 1) % len(shapes)
        else:
            rock_shape = check

    return len(grid) + additional_height

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = get_height_after_number_of_rocks(data, 2022)

    # Part 2
    solution2 = get_height_after_number_of_rocks(data, 1_000_000_000_000)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
