"""
Solution for day 19 of year 2017
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    return tuple(line)

def get_letters(data, get_steps = False):
    pos = [data[0].index('|'),0]
    direction = [0,1]

    nextpos = [pos[0] + direction[0], pos[1] + direction[1]]

    letters = ''
    steps = 0

    while True:
        steps += 1
        pos = nextpos
        char = data[pos[1]][pos[0]]
        if char in '-|ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                letters += char
            nextpos = [pos[0] + direction[0], pos[1] + direction[1]]
        elif char == '+':
            if direction[0] == 0:
                if len(data) <= pos[1] + direction[1] or pos[1] + direction[1] < 0 or data[pos[1] + direction[1]][pos[0] + direction[0]] in ' -':
                    if pos[0] + direction[0] > 0 and data[pos[1]][pos[0] -1] not in ' |':
                        direction = [-1, 0]
                    else:
                        direction = [1, 0]
                nextpos = [pos[0] + direction[0], pos[1] + direction[1]]
            else:
                if len(data[pos[1] + direction[1]]) <= pos[0] + direction[0] or pos[0] + direction[0] < 0 or data[pos[1] + direction[1]][pos[0] + direction[0]] in ' |':
                    if pos[1] + direction[1] > 0 and data[pos[1] - 1][pos[0]] not in ' -':
                        direction = [0, -1]
                    else:
                        direction = [0, 1]
                nextpos = [pos[0] + direction[0], pos[1] + direction[1]]
        else:
            break
    if get_steps:
        return steps
    return letters

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = get_letters(data)

    # Part 2
    solution2 = get_letters(data, True)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

