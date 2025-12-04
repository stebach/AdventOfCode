"""
Solution for day 04 of year 2025
"""

import os
from copy import deepcopy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    return tuple(1 if x == '@' else 0 for x in line.strip())

def adjacentsum(data, x, y):
    result = 0
    for dy in (-1, 0, 1):
        if y + dy < 0 or y + dy >= len(data):
            continue
        for dx in (-1, 0, 1):
            if abs(dx) + abs(dy) == 0 or x + dx < 0 or x + dx >= len(data[0]):
                continue
            result += data[y + dy][x + dx]
    return result

def part1(data):
    result = 0

    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == 1 and adjacentsum(data, col, row) < 4:
                result += 1

    return result

def part2(data):
    result = 0

    result = [[x for x in row] for row in data]

    edited = True
    while edited:
        edited = False
        newresult = deepcopy(result)

        for row in range(len(result)):
            for col in range(len(result[row])):
                adjsum = adjacentsum(result, col, row)
                if result[row][col] == 1 and adjsum < 4:
                    newresult[row][col] = 0
                    edited = True

        result = newresult
    return sum(map(sum, data)) - sum(map(sum, result))

def solve(data):
    # Part 1
    solution1 = part1(data)

    # Part 2
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

