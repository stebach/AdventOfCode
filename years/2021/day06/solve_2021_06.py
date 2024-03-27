"""
Solution for day 06 of year 2021
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    result = {}
    for line in lines:
        line = [int(x) for x in line.strip().split(',')]
        for num in line:
            if not num in result:
                result[num] = 0
            result[num] += 1

    return result

def grow(data, days):
    for day in range(days):
        new_data = {}
        for key in data:
            val = data[key]
            if key == 0:
                new_data[8] = val
                key = 7
            key -= 1
            if not key in new_data:
                new_data[key] = 0
            new_data[key] += val
        data = new_data
    return sum([data[x] for x in data])

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = grow(data, 80)

    # Part 2
    solution2 = grow(data, 256)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

