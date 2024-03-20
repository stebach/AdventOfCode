"""
Solution for day 18 of year 2020
"""

import os
import regex
from copy import deepcopy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    line = line.strip()
    pattern = r'([0-9]+|\*|\+|\(|\))'

    result = regex.findall(pattern, line)

    final_line = []
    fill_line(final_line, result)

    return final_line

def fill_line(line, result):
    while len(result) > 0:
        next = result.pop(0)
        if next == '*':
            line.append(next)
        elif next == '+':
            line.append(next)
        elif next == '(':
            sub = []
            fill_line(sub, result)
            line.append(sub)
        elif next == ')':
            return;
        else:
            line.append(int(next))

def calc(problem, advanced = False):
    problem = deepcopy(problem)
    for pos, x in enumerate(problem):
        if type(x) is list:
            problem[pos] = calc(x, advanced)
    if advanced:
        pos = 1
        while pos < len(problem):
            if problem[pos] == '+':
                problem[pos + 1] += problem[pos - 1]
                problem.pop(pos - 1)
                problem.pop(pos - 1)
                pos -= 2
            pos += 2
    while len(problem) > 1:
        if problem[1] == '+':
            problem[2] += problem[0]
            problem.pop(0)
            problem.pop(0)
        elif problem[1] == '*':
            problem[2] *= problem[0]
            problem.pop(0)
            problem.pop(0)
    return problem[0]

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = sum([calc(x) for x in data])

    # Part 2
    solution2 = sum([calc(x, True) for x in data])

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

