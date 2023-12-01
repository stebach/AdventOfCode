"""
Solution for day 01 of year 2023
"""

import os
import regex

NUMBERS = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(lambda line: line.strip(), inputdata.readlines()))

def get_calibration_value(data, with_strings = False):
    pattern = r'([0-9])'
    if with_strings:
        pattern = r'([0-9]|one|two|three|four|five|six|seven|eight|nine)'

    result = regex.findall(pattern, data, overlapped=True)

    first_number = int(result[0]) if result[0].isdigit() else NUMBERS[result[0]]
    last_number = int(result[-1]) if result[-1].isdigit() else NUMBERS[result[-1]]

    return first_number * 10 + last_number

def part1(data):
    """Solve part 1"""
    return sum(tuple(map(get_calibration_value, data)))

def part2(data):
    """Solve part 2"""
    return (sum(tuple(map(lambda x: get_calibration_value(x, True), data))))

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
