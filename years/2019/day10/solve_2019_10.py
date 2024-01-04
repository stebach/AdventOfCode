"""
Solution for day 10 of year 2019
"""

import os
from math import degrees, atan2

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    result = []
    for y, line in enumerate(lines):
        for x, check in enumerate(line):
            if check == '#':
                result.append((x,y))
    return tuple(result)

def part1(data):
    """Solve part 1"""
    max_found = 0
    for x in data:
        results = set()
        for y in data:
            if y != x:
                dy = y[1] - x[1]
                dx = y[0] - x[0]
                angle = degrees(atan2(dy, dx))
                results.add(angle)
        max_found = max(max_found, len(results))
    return max_found

def part2(data):
    """Solve part 2"""
    max_found = 0
    max_coords = None
    for x in data:
        results = set()
        for y in data:
            if y != x:
                dy = y[1] - x[1]
                dx = y[0] - x[0]
                angle = degrees(atan2(dy, dx))
                results.add(angle)
        if len(results) > max_found:
            max_found = len(results)
            max_coords = x

    results = {}
    for y in data:
        if y != max_coords:
            dy = y[1] - max_coords[1]
            dx = y[0] - max_coords[0]
            angle = degrees(atan2(dy, dx))+ 90
            if angle < 0:
                angle += 360
            if angle not in results:
                results[angle] = []
            results[angle].append(y)
    
    sorted = []
    for key in results:
        targets = [[abs(x[0] - max_coords[0]) + abs(x[1] - max_coords[1]), x] for x in results[key]]
        targets.sort()
        sorted.append([key, targets])

    sorted.sort()

    index = 0
    last_coord = None
    shot = 0
    while shot < 200:
        current_target = sorted[index % len(sorted)]
        index += 1
        if len(current_target[1]) > 0:
            last_coord = current_target[1].pop(0)[1]
            shot += 1

    return last_coord[0] * 100 + last_coord[1]

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
