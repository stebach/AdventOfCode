"""
Solution for day 10 of year 2018
"""

import os
import regex

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return list(map(parse_line, inputdata.readlines()))

def parse_line(line):
    match = regex.findall(r'position=< *([-0-9]+), *([-0-9]+)> velocity=< *([-0-9]+), *([-0-9]+)>',line.strip())
    return [[int(match[0][0]), int(match[0][1])],[int(match[0][2]), int(match[0][3])]]

def draw(data, time):
    data = [[x[0][0] + x[1][0] * time, x[0][1] + x[1][1] * time] for x in data]
    min_x = min([x[0] for x in data])
    max_x = max([x[0] for x in data])
    min_y = min([x[1] for x in data])
    max_y = max([x[1] for x in data])
    return ["".join(["█" if [x, y] in data else " " for x in range(min_x, max_x + 1)]) for y in range(min_y, max_y + 1)]

def parse_lines(lines):
    return [x for x in lines]

def find_time(data):
    time = 0
    dist_x = 0
    dist_y = 0
    last_dist_y = 0
    last_dist_x = 0
    while time < 2 or (last_dist_y >= dist_y and last_dist_x >= dist_x):
        last_dist_x = dist_x
        last_dist_y = dist_y
        time += 1
        check = [[x[0][0] + x[1][0] * time, x[0][1] + x[1][1] * time] for x in data]
        min_x = min([x[0] for x in check])
        max_x = max([x[0] for x in check])
        min_y = min([x[1] for x in check])
        max_y = max([x[1] for x in check])
        dist_x = abs(min_x - max_x)
        dist_y = abs(min_y - max_y)
    return time -1

def part1(data):
    """Solve part 1"""
    return "\n".join(draw(data, find_time(data)))

def part2(data):
    """Solve part 2"""
    return find_time(data)

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
