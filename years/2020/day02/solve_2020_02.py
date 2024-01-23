"""
Solution for day 02 of year 2020
"""

import os
import regex

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    line = line.strip()
    res = regex.findall('^([0-9]+)\-([0-9]+) ([a-z]): ([a-z]+)$', line)
    return (int(res[0][0]), int(res[0][1]), res[0][2], res[0][3])

def check_password(password):
    amount = password[3].count(password[2])
    return amount >= password[0] and amount <= password[1]

def check_password_part2(password):
    return (password[3][password[0]-1] + password[3][password[1]-1]).count(password[2]) == 1

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = sum([check_password(x) for x in data])

    # Part 2
    solution2 = sum([check_password_part2(x) for x in data])

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
