"""
Solution for day 13 of year 2023
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.read())

def parse_lines(lines):
    return [x.split("\n") for x in lines.split("\n\n")]

def start_of_reflection(pattern, rotate=False, smudge=False):
    if rotate:
        pattern = ["".join([y[x] for y in pattern]) for x in range(len(pattern[0]))]
    for row in range(len(pattern) - 1):
        diff = sum([1 for x,y in zip(pattern[row], pattern[row + 1]) if x != y])
        if diff == 0 or (diff < 2 and smudge):
            match = True
            for check in range(1, min(row, len(pattern) - row - 2) + 1):
                diff = diff + sum([1 for x,y in zip(pattern[row - check], pattern[row + check + 1]) if x != y])
                if (diff > 0 and not smudge) or diff > 1:
                    match = False
                    break
            if match and (not smudge or diff == 1):
                return row
    return -1

def part1(data):
    """Solve part 1"""
    result = 0
    for pattern in data:
        start = start_of_reflection(pattern)
        if start == -1:
            start = start_of_reflection(pattern, rotate=True)
            result = result + start + 1
        else:
            result = result + (start + 1) * 100
    return result

def part2(data):
    """Solve part 2"""
    result = 0
    for pattern in data:
        start = start_of_reflection(pattern, smudge=True)
        if start == -1:
            start = start_of_reflection(pattern, rotate=True, smudge=True)
            result = result + start + 1
        else:
            result = result + (start + 1) * 100
    return result

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
