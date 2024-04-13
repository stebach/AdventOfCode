"""
Solution for day 25 of year 2021
"""

import os
import time

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    result = {
        'width': 0,
        'height': 0,
        'moves': 0,
        'right': set([]),
        'down': set([])
    }
    for (y, line) in enumerate(lines):
        line = line.strip()
        result['width'] = len(line)
        for (x, char) in enumerate(line):
            if char == '>':
                result['right'].add((x, y))
            elif char == 'v':
                result['down'].add((x, y))
        result['height'] += 1
    return result

def step(data):
    right = set([])
    down = set([])
    moves = 0

    for check in data['right']:
        moved = (0 if check[0] + 1 == data['width'] else check[0] + 1, check[1])
        if moved not in data['right'] and moved not in data['down']:
            moves += 1
            right.add(moved)
        else:
            right.add(check)
    data['right'] = right

    for check in data['down']:
        moved = (check[0], 0 if check[1] + 1 == data['height'] else check[1] + 1)
        if moved not in data['right'] and moved not in data['down']:
            moves += 1
            down.add(moved)
        else:
            down.add(check)
    data['down'] = down

    data['moves'] = moves

    return data

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    steps = 0
    data['moves'] = 1
    while data['moves'] > 0:
        step(data)
        steps += 1
    solution1 = steps
    print(solution1)
    exit()
    # Part 2
    solution2 = None

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
