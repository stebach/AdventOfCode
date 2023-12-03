"""
Solution for day 03 of year 2023
"""

import os
import regex
import math;

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(lambda line: line.strip(), inputdata.readlines()))

def find_numbers(puzzle_input):
    numbers = []
    for line in range(len(puzzle_input)):
        linenumbers = regex.finditer('([0-9]+)', puzzle_input[line])
        for match in linenumbers:
            symbols = []
            for rownum in range(3):
                if rownum + line - 1 >= len(puzzle_input):
                    continue
                row = puzzle_input[rownum + line - 1]
                symbolsaround = regex.finditer('[^0-9\.]', row[max([0, match.start() - 1]):min([match.end() + 1, len(row)])])
                for symbolmatch in symbolsaround:
                    symbols = symbols + [[symbolmatch.group(),symbolmatch.start()+max([0, match.start() - 1]),rownum + line - 1]]
            numbers += [[int(match.group()), symbols]]
    return numbers

def part1(data):
    """Solve part 1"""
    return sum([x[0] if len(x[1]) > 0 else 0 for x in data])

def part2(data):
    """Solve part 2"""
    gears = {}
    for number in data:
        for gear in number[1]:
            if gear[0] == '*':
                key = "_".join(map(str, gear))
                if not key in gears:
                    gears[key] = []
                gears[key] = gears[key] + [number[0]]
    return sum(map(lambda x: math.prod(x) if len(x) == 2 else 0, gears.values()))

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    numbers = find_numbers(puzzle_input)
    solutions = solve(numbers)
    print("\n".join(str(solution) for solution in solutions))
