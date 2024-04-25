"""
Solution for day 18 of year 2022
"""

import os
from copy import deepcopy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    return tuple([int(x) for x in line.strip().split(',')])

def get_surface(data):
    connected_sides = 0
    for x in range(0, len(data) - 1):
        for y in range(x+1, len(data)):
            if abs(data[x][0] - data[y][0]) + abs(data[x][1] - data[y][1]) + abs(data[x][2] - data[y][2]) == 1:
                connected_sides += 1

    return len(data) * 6 - connected_sides * 2

def get_exterior_surface(data):
    edge = [y for y in data if y[0] == min([x[0] for x in data])][0]

    directions = (
        (-1, 0, 0 ),
        (1, 0, 0 ),
        (0, -1, 0 ),
        (0, 1, 0 ),
        (0, 0, -1 ),
        (0, 0, 1 ),
    )

    wrapper = set([
        (edge[0] + directions[0][0], edge[1] + directions[1][0], edge[2] + directions[2][0])
    ])

    to_check = deepcopy(wrapper)
    new_wrappers = set([])

    while len(to_check) > 0:
        new_wrappers.clear()
        for check in to_check:
            for direction in directions:
                directed = (check[0] + direction[0], check[1] + direction[1], check[2] + direction[2])
                if directed in wrapper or directed in data:
                    continue
                for coord in data:
                    if coord[0] >= directed[0] - 1 and coord[0] <= directed[0] + 1 and coord[1] >= directed[1] - 1 and coord[1] <= directed[1] + 1 and coord[2] >= directed[2] - 1 and coord[2] <= directed[2] + 1:
                        new_wrappers.add(directed)
        to_check.clear()
        for x in new_wrappers:
            to_check.add(x)
            wrapper.add(x)

    surfaces = 0
    for coord in data:
        for w in wrapper:
            if abs(coord[0] - w[0]) + abs(coord[1] - w[1]) + abs(coord[2] - w[2]) == 1:
                surfaces += 1

    return surfaces

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = get_surface(data)

    # Part 2
    solution2 = get_exterior_surface(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

