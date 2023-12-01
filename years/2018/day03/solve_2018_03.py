"""
Solution for day 03 of year 2018
"""

import os
import re

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    match = re.search(r'^#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)$', line.strip())
    return tuple((int(match.group(1)),int(match.group(2)),int(match.group(3)),int(match.group(4)),int(match.group(5))))

def get_grid(data):
    grid = []

    for row in data:
        while len(grid) < row[1] + row[3]:
            grid.append([])
        for x in range(row[3]):
            while len(grid[x + row[1]]) < row[2] + row[4]:
                grid[x + row[1]].append(0)
            for y in range(row[4]):
                grid[x + row[1]][y + row[2]] += 1
    return grid

def part1(data):
    """Solve part 1"""
    grid = get_grid(data)
    return sum(list(map(lambda item: sum(map(lambda item2 : 1 if item2 > 1 else 0, item)), grid)))

def part2(data):
    """Solve part 2"""
    grid = get_grid(data)
    for row in data:
        found = True
        for x in range(row[3]):
            for y in range(row[4]):
                if grid[x + row[1]][y + row[2]] > 1:
                    found = False
                    break
            if not found:
                break
        if found:
            break

    return row[0]

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
