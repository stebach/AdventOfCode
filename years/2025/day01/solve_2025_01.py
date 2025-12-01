"""
Solution for day 01 of year 2025
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    line = line.strip()
    return (1 if line[0] == "R" else -1, int(line[1:]))

def count_zeroes(lines, count_clicks = False, start = 50):
    zeroes = 0
    pos = start
    for direction, length in lines:
        pos += direction * length
        if count_clicks and (pos < 1 or pos > 99):
            zeroes += abs(pos // 100)
            if direction == -1 and pos - direction * length == 0:
                zeroes -= 1
            if direction == -1 and pos % 100 == 0:
                zeroes += 1
        pos = pos % 100
        if not count_clicks and pos == 0:
            zeroes += 1

    return zeroes

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = count_zeroes(data)
    # Part 2
    solution2 = count_zeroes(data, True)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
