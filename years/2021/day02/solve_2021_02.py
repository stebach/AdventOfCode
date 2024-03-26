"""
Solution for day 02 of year 2021
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    line = line.strip().split(' ')
    return tuple([line[0], int(line[1])])

def get_horizontal_position(data):
    x = 0
    y = 0
    for movement, amount in data:
        if movement == "up":
            y -= amount
        elif movement == "down":
            y += amount
        elif movement == "forward":
            x += amount
    return x * y

def get_horizontal_position_using_aim(data):
    x = 0
    y = 0
    aim = 0
    for movement, amount in data:
        if movement == "up":
            aim -= amount
        elif movement == "down":
            aim += amount
        elif movement == "forward":
            x += amount
            y += aim * amount
    return x * y

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = get_horizontal_position(data)

    # Part 2
    solution2 = get_horizontal_position_using_aim(data)
    print(solution2)
    exit()
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
