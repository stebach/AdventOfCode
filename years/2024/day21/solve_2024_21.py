"""
Solution for day 21 of year 2024
"""

import os
from functools import lru_cache 

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    return tuple(line.strip())

def get_complexity(data, recursion = 2):
    pos = (2, 3)
    keypad = {
        '7': (0, 0),
        '8': (1, 0),
        '9': (2, 0),
        '4': (0, 1),
        '5': (1, 1),
        '6': (2, 1),
        '1': (0, 2),
        '2': (1, 2),
        '3': (2, 2),
        '0': (1, 3),
        'A': (2, 3)
    }
    forbidden = (0, 3)

    result = 0
    for key in data:
        result += get_fastest(pos, keypad[key], forbidden, recursion)
        pos = keypad[key]

    return result * int("".join(data[:-1]))

@lru_cache
def get_fastest(pos, new_pos, forbidden, recursion):
    paths = []
    if (pos[0], new_pos[1]) != forbidden:
        path = []
        tmp_pos = pos
        while tmp_pos[1] < new_pos[1]:
            path.append(((tmp_pos[0], tmp_pos[1] + 1),'v'))
            tmp_pos = (tmp_pos[0], tmp_pos[1] + 1)
        while tmp_pos[1] > new_pos[1]:
            path.append(((tmp_pos[0], tmp_pos[1] - 1),'^'))
            tmp_pos = (tmp_pos[0], tmp_pos[1] - 1)

        while tmp_pos[0] < new_pos[0]:
            path.append(((tmp_pos[0] + 1, tmp_pos[1]),'>'))
            tmp_pos = (tmp_pos[0] + 1, tmp_pos[1])
        while tmp_pos[0] > new_pos[0]:
            path.append(((tmp_pos[0] - 1, tmp_pos[1]),'<'))
            tmp_pos = (tmp_pos[0] - 1, tmp_pos[1])
        paths.append(path)
    if (new_pos[0], pos[1]) != forbidden:
        path = []
        tmp_pos = pos
        while tmp_pos[0] < new_pos[0]:
            path.append(((tmp_pos[0] + 1, tmp_pos[1]),'>'))
            tmp_pos = (tmp_pos[0] + 1, tmp_pos[1])
        while tmp_pos[0] > new_pos[0]:
            path.append(((tmp_pos[0] - 1, tmp_pos[1]),'<'))
            tmp_pos = (tmp_pos[0] - 1, tmp_pos[1])

        while tmp_pos[1] < new_pos[1]:
            path.append(((tmp_pos[0], tmp_pos[1] + 1),'v'))
            tmp_pos = (tmp_pos[0], tmp_pos[1] + 1)
        while tmp_pos[1] > new_pos[1]:
            path.append(((tmp_pos[0], tmp_pos[1] - 1),'^'))
            tmp_pos = (tmp_pos[0], tmp_pos[1] - 1)
        if path not in paths:
            paths.append(path)

    if recursion == 0:
        return min([len(x) for x in paths]) + 1

    keypad = {
        '^': (1, 0),
        'A': (2, 0),
        '<': (0, 1),
        'v': (1, 1),
        '>': (2, 1),
    }

    fastest = 10000000000000
    for path in paths:
        result = 0
        current_pos = (2,0)
        for step in path:
            result += get_fastest(current_pos, keypad[step[1]], (0, 0), recursion - 1)
            current_pos = keypad[step[1]]
        result += get_fastest(current_pos, (2,0), (0, 0), recursion - 1)

        if result < fastest:
            fastest = result
    return fastest

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = sum([get_complexity(x) for x in data])

    # Part 2
    solution2 = sum([get_complexity(x, 25) for x in data])

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
