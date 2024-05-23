"""
Solution for day 02 of year 2016
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    return tuple([*line.strip()])

def get_code(data):
    pos = 5
    code = 0

    for line in data:
        for move in line:
            if move == 'U':
                if pos > 3:
                    pos -= 3
            elif move == 'L':
                if (pos -1) % 3 != 0:
                    pos -= 1
            elif move == 'R':
                if pos % 3 != 0:
                    pos += 1
            elif move == 'D':
                if pos < 7:
                    pos += 3
            else:
                print('UNKNOWN MOVE: ' + move)
                exit()
        code = code * 10 + pos

    return code

def get_code_two(data):
    pos = 5
    code = ''

    for line in data:
        for move in line:
            if move == 'U':
                if pos in (3, 13):
                    pos -= 2
                elif pos in (6,7,8,10,11,12):
                    pos -= 4
            elif move == 'L':
                if pos in (6,9,3,7,11,4,8,12):
                    pos -= 1
            elif move == 'R':
                if pos in (2,3,5,6,7,8,10,11):
                    pos += 1
            elif move == 'D':
                if pos in (1, 11):
                    pos += 2
                elif pos in (2,3,4,6,7,8):
                    pos += 4
            else:
                print('UNKNOWN MOVE: ' + move)
                exit()
        code += hex(pos)[2:].upper()
    return code

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = get_code(data)

    # Part 2
    solution2 = get_code_two(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

