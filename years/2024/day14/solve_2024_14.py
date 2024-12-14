"""
Solution for day 14 of year 2024
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    return tuple([tuple([int(y) for y in x[2:].split(',')]) for x in line.strip().split(' ')])

def get_safety_factor(data, width = 101, height = 103):
    positions = [[(x[0][0] + x[1][0] * 100) % width, (x[0][1] + x[1][1] * 100) % height] for x in data]
    middle = [width // 2, height // 2]
    quadrants = [0,0,0,0]
    for position in positions:
        if position[0] < middle[0]:
            if position[1] < middle[1]:
                quadrants[0] += 1
            elif position[1] > middle[1]:
                quadrants[2] += 1
        elif position[0] > middle[0]:
            if position[1] < middle[1]:
                quadrants[1] += 1
            elif position[1] > middle[1]:
                quadrants[3] += 1

    return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]

def find_egg(data):
    center_coords = (50, 51)
    for i in range(1000000):
        positions = tuple([tuple([(x[0][0] + x[1][0] * i) % 101, (x[0][1] + x[1][1] * i) % 103]) for x in data])
        if (sum([1 for x in positions if (x[0] + 1, x[1]) in positions]) > 100):
            return i

def solve(data, width = 101, height = 103):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = get_safety_factor(data, width, height)

    # Part 2
    solution2 = find_egg(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
