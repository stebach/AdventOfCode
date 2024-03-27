"""
Solution for day 07 of year 2021
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

def optimal_fuel_for_alignment(data):
    val = 100000000000000
    for pos in range(min(data), max(data) +1):
        check = sum([abs(x - pos) * data[x] for x in data])
        if check < val:
            val = check
        else:
            break
    return val

def optimal_fuel_for_alignment_adjusted(data):
    val = 100000000000000
    for pos in range(min(data), max(data) +1):
        check = sum([int((abs(x - pos) * (abs(x - pos) + 1)) / 2) * data[x] for x in data])
        if check < val:
            val = check
        else:
            break
    return val

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = optimal_fuel_for_alignment(data)

    # Part 2
    solution2 = optimal_fuel_for_alignment_adjusted(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
